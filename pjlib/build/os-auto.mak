# pjlib/build/os-auto.mak.  Generated from os-auto.mak.in by configure.

# Determine OS specific files
AC_OS_OBJS=ioqueue_select.o file_access_unistd.o file_io_ansi.o os_core_unix.o os_error_unix.o os_time_unix.o os_timestamp_posix.o sock_qos_bsd.o guid_simple.o

#
# PJLIB_OBJS specified here are object files to be included in PJLIB
# (the library) for this specific operating system. Object files common 
# to all operating systems should go in Makefile instead.
#
export PJLIB_OBJS +=    $(AC_OS_OBJS) \
                        addr_resolv_sock.o \
                        log_writer_stdout.o \
                        os_timestamp_common.o \
                        pool_policy_malloc.o sock_bsd.o sock_select.o

#
# TEST_OBJS are operating system specific object files to be included in
# the test application.
#
export TEST_OBJS +=     main.o

#
# Additional LDFLAGS for pjlib-test
#
# Disabled, as this causes duplicated LDFLAGS, which may raise linking errors
#export TEST_LDFLAGS +=  -lopus -lm -lrt -lpthread  -lasound  -L/usr/local/lib -lavdevice -lavformat -lavcodec -lswscale -lavutil -lopencore-amrnb -lopencore-amrwb

#
# TARGETS are make targets in the Makefile, to be executed for this given
# operating system.
#
export TARGETS      =   $(PJLIB_LIB) $(PJLIB_SONAME)
export TARGETS_EXE  =   $(TEST_EXE)
