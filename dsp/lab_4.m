fs_dst = 20e3;
[src, fs_src] = audioread("input.wav");

% Test sound before compression
% sound(src, fs_src)
src = resample(src, fs_dst, fs_src);

padding = ceil(length(src) / fs_dst) * fs_dst - length(src);
src = [src; zeros(padding, 1)];
dst = zeros(length(src), 1);

for i = 1 : (length(src) / fs_dst)
    st = 1 + fs_dst * (i - 1);
    en = st + fs_dst - 1; 

    frame = src(st : en, 1);
    frame = fftshift(fft(frame));
    frame([1:6600 9601:10400 13401:20000]) = 0;
    % Always pure real, because signal is even
    frame = real(ifft(ifftshift(frame)));

    dst(st : en, 1) = frame;
end

% Test sound after compression
sound(dst, fs_dst);

audiowrite("output.wav", dst, fs_dst);
