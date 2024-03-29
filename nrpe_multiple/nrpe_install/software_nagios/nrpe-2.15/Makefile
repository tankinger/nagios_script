###############################
# Makefile for NRPE
#
# Last Modified: 03-14-2007
###############################


# Source code directories
SRC_BASE=./src/
SRC_INCLUDE=./include/

CC=gcc
CFLAGS=-g -O2 -I/usr/include/openssl -I/usr/include -DHAVE_CONFIG_H
LDFLAGS= -L/usr/lib/x86_64-linux-gnu  -lssl -lcrypto

prefix=/usr/local/nagios
exec_prefix=${prefix}
CFGDIR=${prefix}/etc
BINDIR=${exec_prefix}/bin
SBINDIR=${exec_prefix}/sbin
LIBEXECDIR=${exec_prefix}/libexec
INSTALL=/usr/bin/install -c
NAGIOS_INSTALL_OPTS=-o nagios -g nagios
NRPE_INSTALL_OPTS=-o nagios -g nagios

INIT_DIR=@init_dir@
INIT_OPTS=-o root -g root


all:
	cd $(SRC_BASE); $(MAKE) ; cd ..

	@echo ""
	@echo "*** Compile finished ***"
	@echo ""
	@echo "If the NRPE daemon and client compiled without any errors, you"
	@echo "can continue with the installation or upgrade process."
	@echo ""
	@echo "Read the PDF documentation (NRPE.pdf) for information on the next"
	@echo "steps you should take to complete the installation or upgrade."
	@echo ""
nrpe:
	cd $(SRC_BASE); $(MAKE) ; cd ..

check_nrpe:
	cd $(SRC_BASE); $(MAKE) ; cd ..


install-plugin:
	cd $(SRC_BASE) && $(MAKE) $@

install-daemon:
	cd $(SRC_BASE) && $(MAKE) $@

install:
	cd $(SRC_BASE) && $(MAKE) $@

install-xinetd:
	$(INSTALL) -m 644 sample-config/nrpe.xinetd /etc/xinetd.d/nrpe 

install-daemon-config:
	$(INSTALL) -m 775 $(NAGIOS_INSTALL_OPTS) -d $(DESTDIR)$(CFGDIR)
	$(INSTALL) -m 644 $(NRPE_INSTALL_OPTS) sample-config/nrpe.cfg $(DESTDIR)$(CFGDIR)

solaris-package:
	@if [ `uname -s` != "SunOS" ] ; then \
		echo "It is recommended you be running on Solaris to build a Solaris package"; \
	else \
		cd package/solaris; $(MAKE) build ; $(MAKE) pkg ; cd ../..; \
	fi

clean:
	cd $(SRC_BASE); $(MAKE) $@ ; cd ..
	cd package/solaris; $(MAKE) $@ ; cd ../..
	rm -f core
	rm -f *~ */*~

distclean: clean
	cd $(SRC_BASE); $(MAKE) $@ ; cd ..
	cd package/solaris; $(MAKE) $@ ; cd ../..
	rm -f config.log config.status config.cache nrpe.cfg nrpe.xinetd subst $(SRC_INCLUDE)/config.h init-script init-script.debian init-script.freebsd init-script.suse
	rm -f sample-config/*.cfg sample-config/*.xinetd
	rm -f Makefile

devclean: distclean

