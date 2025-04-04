#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v23
# autospec commit: 247c192
#
Name     : R-Cubist
Version  : 0.5.0
Release  : 66
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/Cubist_0.5.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/Cubist_0.5.0.tar.gz
Summary  : Rule- And Instance-Based Regression Modeling
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Cubist-lib = %{version}-%{release}
Requires: R-reshape2
BuildRequires : R-reshape2
BuildRequires : buildreq-R

%description
corrections.

%package lib
Summary: lib components for the R-Cubist package.
Group: Libraries

%description lib
lib components for the R-Cubist package.


%prep
%setup -q -n Cubist
pushd ..
cp -a Cubist buildavx2
popd
pushd ..
cp -a Cubist buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743782367

%install
export SOURCE_DATE_EPOCH=1743782367
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Cubist/DESCRIPTION
/usr/lib64/R/library/Cubist/INDEX
/usr/lib64/R/library/Cubist/Meta/Rd.rds
/usr/lib64/R/library/Cubist/Meta/features.rds
/usr/lib64/R/library/Cubist/Meta/hsearch.rds
/usr/lib64/R/library/Cubist/Meta/links.rds
/usr/lib64/R/library/Cubist/Meta/nsInfo.rds
/usr/lib64/R/library/Cubist/Meta/package.rds
/usr/lib64/R/library/Cubist/Meta/vignette.rds
/usr/lib64/R/library/Cubist/NAMESPACE
/usr/lib64/R/library/Cubist/NEWS.md
/usr/lib64/R/library/Cubist/R/Cubist
/usr/lib64/R/library/Cubist/R/Cubist.rdb
/usr/lib64/R/library/Cubist/R/Cubist.rdx
/usr/lib64/R/library/Cubist/doc/cubist.R
/usr/lib64/R/library/Cubist/doc/cubist.Rmd
/usr/lib64/R/library/Cubist/doc/cubist.html
/usr/lib64/R/library/Cubist/doc/index.html
/usr/lib64/R/library/Cubist/help/AnIndex
/usr/lib64/R/library/Cubist/help/Cubist.rdb
/usr/lib64/R/library/Cubist/help/Cubist.rdx
/usr/lib64/R/library/Cubist/help/aliases.rds
/usr/lib64/R/library/Cubist/help/paths.rds
/usr/lib64/R/library/Cubist/html/00Index.html
/usr/lib64/R/library/Cubist/html/R.css
/usr/lib64/R/library/Cubist/tests/testthat.R
/usr/lib64/R/library/Cubist/tests/testthat/_snaps/basic-execution.md
/usr/lib64/R/library/Cubist/tests/testthat/test-basic-execution.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/Cubist/libs/Cubist.so
/V4/usr/lib64/R/library/Cubist/libs/Cubist.so
/usr/lib64/R/library/Cubist/libs/Cubist.so
