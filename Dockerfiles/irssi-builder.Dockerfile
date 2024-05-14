FROM fedora:39

RUN dnf -y update
RUN dnf -y install meson ninja* git gcc glib2-devel utf8proc* ncurses* perl-Ext*

RUN git clone https://github.com/Grallistrix/irssi

WORKDIR /irssi

RUN meson Build
RUN ninja -C /irssi/Build
