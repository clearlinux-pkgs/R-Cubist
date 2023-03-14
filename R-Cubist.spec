#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Cubist
Version  : 0.4.2.1
Release  : 58
URL      : https://cran.r-project.org/src/contrib/Cubist_0.4.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Cubist_0.4.2.1.tar.gz
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
cd %{_builddir}/Cubist

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678814090

%install
export SOURCE_DATE_EPOCH=1678814090
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/Cubist/libs/Cubist.so
/usr/lib64/R/library/Cubist/libs/Cubist.so.avx2
/usr/lib64/R/library/Cubist/libs/Cubist.so.avx512
