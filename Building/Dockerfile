FROM ubuntu

RUN apt update
RUN apt -y install git meson ninja* libglib2.0-dev libutf8proc* ncurses-dev

RUN git clone https://github.com/Grallistrix/irssi

WORKDIR /irssi

RUN meson build
RUN ninja -C /irssi/build