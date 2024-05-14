FROM fedora:latest 

RUN dnf install -y git
RUN dnf install -y meson ninja* gcc  glib2-devel utf8proc* ncurses* perl-Ext*
RUN git clone https://github.com/Grallistrix/irssi

WORKDIR /irssi 

RUN meson build && \
ninja -C ./build
