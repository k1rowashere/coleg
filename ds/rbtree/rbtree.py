from __future__ import annotations
import curses
from curses import ascii
import time
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any


class Color(Enum):
    RED = 0
    BLACK = 1


@dataclass
class Node:
    value: Any
    left: Optional[Node]
    right: Optional[Node]
    parent: Optional[Node]
    color: Color

    @staticmethod
    def new_black(value):
        return Node(value, None, None, None, Color.BLACK)

    @staticmethod
    def new_red(value):
        return Node(value, None, None, None, Color.RED)

    def insert(self, value) -> Node | None:
        if value == self.value:
            return None
        elif value < self.value:
            if self.left is None:
                self.left = Node.new_red(value)
                self.left.parent = self
                return self.left
            else:
                return self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node.new_red(value)
                self.right.parent = self
                return self.right
            else:
                return self.right.insert(value)

    def get_uncle(self) -> Node | None:
        if self.parent is None or self.parent.parent is None:
            return None

        grandparent = self.parent.parent
        if grandparent.left == self.parent:
            return grandparent.right
        else:
            return grandparent.left

    def rotate_left(self):
        if self.right is None:
            return

        if self.parent:
            if self.parent.right == self:
                self.parent.right = self.right
            else:
                self.parent.left = self.right

        self.right.parent = self.parent
        self.parent = self.right

        self.right.left, self.right = self, self.right.left
        if self.right:
            self.right.parent = self

    def rotate_right(self):
        if self.left is None:
            return

        if self.parent:
            if self.parent.right == self:
                self.parent.right = self.left
            else:
                self.parent.left = self.left

        self.left.parent = self.parent
        self.parent = self.left

        self.left.right, self.left = self, self.left.right
        if self.left:
            self.left.parent = self

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        return max(left_height, right_height) + 1

    def node_count(self):
        left = self.left.node_count() if self.left else 0
        right = self.right.node_count() if self.right else 0

        return left + right + 1

    def black_height(self):
        counter = 0
        head = self
        while (True):
            head = head.left
            if head is None:
                return counter + 1
            if head.color == Color.BLACK:
                counter += 1

    def find(self, value) -> Node | None:
        if self.value == value:
            return self
        elif value < self.value:
            return self.left.find(value) if self.left else None
        else:
            return self.right.find(value) if self.right else None


class RbTree:
    root: Optional[Node]

    def __init__(self):
        self.root = None

    def height(self) -> int:
        return self.root.height() if self.root else 0

    def node_count(self) -> int:
        return self.root.node_count() if self.root else 0

    def black_height(self) -> int:
        return self.root.black_height() if self.root else 0

    def find(self, value) -> Node | None:
        return self.root.find(value) if self.root else None

    def contains(self, value) -> bool:
        return self.find(value) is not None

    def insert(self, value) -> Node | None:
        if self.root is None:
            self.root = Node.new_black(value)
            return self.root

        inserted_node = self.root.insert(value)

        if inserted_node:
            self.insert_fixup(inserted_node)

        return inserted_node

    def insert_fixup(self, node: Node):
        # case 1: node is root -> set to black
        if node.parent is None:
            node.color = Color.BLACK
            return

        parent = node.parent

        # case 2: parent is black -> do nothing
        if parent.color == Color.BLACK:
            return

        # case 3: parent is root
        if parent.parent is None:
            node.parent.color = Color.BLACK
            return

        grandparent = parent.parent
        uncle = node.get_uncle()

        # parent is red and not root

        # case 3: uncle is red -> recolor then fixup grandparent
        if uncle and uncle.color == Color.RED:
            parent.color = Color.BLACK
            uncle.color = Color.BLACK
            grandparent.color = Color.RED
            self.insert_fixup(grandparent)
            return

        # uncle is black

        # case 4: node is inner child -> rotate with parent
        if grandparent.left == parent and parent.right == node:
            parent.rotate_left()
            node, parent = parent, node
        elif grandparent.right == parent and parent.left == node:
            parent.rotate_right()
            node, parent = parent, node

        # case 5: node is outer child -> rotate so parent becomes grandparent
        grandparent.color = Color.RED
        parent.color = Color.BLACK

        if grandparent.left == parent:
            grandparent.rotate_right()
        else:
            grandparent.rotate_left()

        if grandparent == self.root:
            self.root = parent


def main(stdscr):
    def print_stats():
        msg = ('Dictionary stats:\n'
               f'    Dictionary size = {dictionary.node_count()}\n'
               f'    Tree height = {dictionary.height()}\n'
               f'    Black height = {dictionary.black_height()}\n'
               '-----------------------------------------------\n')
        stdscr.addstr(0, 0, msg)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    curses.curs_set(1)
    curses.use_default_colors()
    curses.echo()

    dictionary = RbTree()
    word = ""

    stdscr.addstr('Loading dictionary...')
    stdscr.refresh()
    with open('dictionary.txt') as word_file:
        for line in word_file.read().split():
            dictionary.insert(line.lower())

    print_stats()
    stdscr.addstr('Find word: ')
    stdscr.refresh()
    mark = curses.getsyx()

    while True:
        stdscr.addstr(mark[0] + 1, 0,
                      'Word In Dictionary?: '
                      f'{dictionary.contains(word.lower())}\n'
                      )
        stdscr.addstr('Press <Enter> to insert word, <ESC> to exit')
        stdscr.move(mark[0], mark[1] + len(word))

        c = stdscr.getch()
        match c:
            case ascii.ESC:  # exit program
                stdscr.clear()
                stdscr.addstr('Program Exiting... Goodbye!')
                stdscr.refresh()
                time.sleep(1)
                return
            case ascii.NL:  # insert into dictionary
                if dictionary.insert(word.lower()):
                    stdscr.addstr(
                        mark[0] + 1, 0,
                        'Word inserted into dictionary.\n',
                        curses.color_pair(2)
                    )
                    with open('dictionary.txt', 'a') as word_file:
                        word_file.write(f'\n{word.lower()}')
                else:
                    stdscr.addstr(
                        mark[0] + 1, 0,
                        'Word already in dictionary. Not inserted.\n',
                        curses.color_pair(1)
                    )
                stdscr.refresh()
                time.sleep(1)
                print_stats()
            case curses.KEY_BACKSPACE:
                word = word[:-1]
                stdscr.addstr(mark[0], mark[1] + len(word), ' ')
            case _:
                word += chr(c)


if __name__ == '__main__':
    curses.wrapper(main)
