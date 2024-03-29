###################################
# Makefile for NRPE Solaris Package
#
# Last Modified: 2 Dec 2011
###################################

TARGET_OS=Linux
TARGET_VER=3.2.0-4-amd64
TARGET_ARCH=unknown
TARGET_PLATFORM=

SOLARIS_CONFIG_OPTS=--prefix=/opt/nagios --sysconfdir=/etc/nagios --enable-command-args

PKG_NAME=NGOSnrpe
PKG_VERSION=2.15
PKG_FILE=nrpe-$(PKG_VERSION)-$(TARGET_PLATFORM)-$(TARGET_ARCH)-local

TOPDIR=../../
PKGDIR=./pkg
SRCDIR=./build/src
INSTALLDIR=./install
ABSINSTALLDIR=/home/nrpe_install/software_nagios/nrpe-2.15/package/solaris/install

build:
	if [ ! -d build ] ; then mkdir build ; fi
	if [ ! -d install ] ; then mkdir install ; fi
	cd build; ../../../configure $(SOLARIS_CONFIG_OPTS); $(MAKE) all; DESTDIR=$(ABSINSTALLDIR) $(MAKE) install install-daemon-config

prototype: $(PKGDIR)
	@echo "i pkginfo" > $(PKGDIR)/prototype
	@echo "i copyright=../$(TOPDIR)/LEGAL" >> $(PKGDIR)/prototype
	@echo "i preinstall" >> $(PKGDIR)/prototype
	@echo "i i.config" >> $(PKGDIR)/prototype
	@echo "i r.config" >> $(PKGDIR)/prototype
	@echo "i i.manifest=/usr/sadm/install/scripts/i.manifest" >> $(PKGDIR)/prototype
	@echo "i r.manifest=/usr/sadm/install/scripts/r.manifest" >> $(PKGDIR)/prototype
	@echo "d none /etc/nagios 0755 nagios nagios" >> $(PKGDIR)/prototype
	@echo "f config /etc/nagios/nrpe.cfg=$(INSTALLDIR)/etc/nagios/nrpe.cfg 0600 nagios nagios" >> $(PKGDIR)/prototype
	@echo "d none /opt/nagios/bin 0755 nagios bin" >> $(PKGDIR)/prototype
	@echo "f none /opt/nagios/bin/nrpe=$(SRCDIR)/nrpe 0755 nagios bin" >> $(PKGDIR)/prototype
	@echo "d none /opt/nagios/libexec 0755 nagios bin" >> $(PKGDIR)/prototype
	@echo "f none /opt/nagios/libexec/check_nrpe=$(SRCDIR)/check_nrpe 0755 nagios bin" >> $(PKGDIR)/prototype
	@echo "f none /lib/svc/method/nrpe=$(PKGDIR)/nrpe 0555 root bin" >> $(PKGDIR)/prototype
	@echo "d none /var/svc/manifest/application/nagios 0755 root sys" >> $(PKGDIR)/prototype
	@echo "f manifest /var/svc/manifest/application/nagios/nrpe.xml=$(PKGDIR)/nrpe.xml 0444 root sys" >> $(PKGDIR)/prototype

pkginfo: $(PKGDIR)
	@echo PKG="$(PKG_NAME)" > $(PKGDIR)/pkginfo
	@echo NAME="Nagios Remote Plugin Executor $(PKG_VERSION)" >> $(PKGDIR)/pkginfo
	@echo VERSION="$(PKG_VERSION)" >> $(PKGDIR)/pkginfo
	@echo ARCH="$(TARGET_ARCH)" >> $(PKGDIR)/pkginfo
	@echo CATEGORY="utility" >> $(PKGDIR)/pkginfo
	@echo CLASSES="none config manifest" >> $(PKGDIR)/pkginfo
	@echo VENDOR="www.nagios.org" >> $(PKGDIR)/pkginfo
	@echo EMAIL="nagios-users@lists.sourceforge.net" >> $(PKGDIR)/pkginfo
	@echo ISTATES="S s 1 2 3" >> $(PKGDIR)/pkginfo
	@echo RSTATES="S s 1 2 3" >> $(PKGDIR)/pkginfo
	@echo BASEDIR="/" >> $(PKGDIR)/pkginfo

$(PKG_FILE): pkginfo prototype
	pkgmk -o -d $(PKGDIR) -f $(PKGDIR)/prototype -r .
	pkgtrans ./pkg $(PKG_FILE) $(PKG_NAME)

pkg: $(PKG_FILE)

all: pkg

clean: 
	rm -rf build install package
	rm -rf $(PKGDIR)/$(PKG_NAME)
	rm -f $(PKGDIR)/prototype $(PKGDIR)/pkginfo
	rm -f $(PKGDIR)/$(PKG_FILE)
	rm -f core
	rm -f *~ */*~

distclean: clean
	rm -f Makefile
	rm -f config.log

devclean: distclean

