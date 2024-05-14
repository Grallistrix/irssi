FROM fedora:39
RUN dnf -y update
RUN dnf -y install meson ninja* git gcc glib2-devel utf8proc* ncurses* perl-Ext*

WORKDIR /irssi

RUN meson Building
RUN ninja -C /irssi/Building