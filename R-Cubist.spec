#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Cubist
Version  : 0.2.3
Release  : 36
URL      : https://cran.r-project.org/src/contrib/Cubist_0.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Cubist_0.2.3.tar.gz
Summary  : Rule- And Instance-Based Regression Modeling
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Cubist-lib = %{version}-%{release}
Requires: R-reshape2
BuildRequires : R-reshape2
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-Cubist package.
Group: Libraries

%description lib
lib components for the R-Cubist package.


%prep
%setup -q -c -n Cubist
cd %{_builddir}/Cubist

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589582695

%install
export SOURCE_DATE_EPOCH=1589582695
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Cubist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Cubist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Cubist
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Cubist || :


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
/usr/lib64/R/library/Cubist/NEWS.Rd
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Cubist/libs/Cubist.so
/usr/lib64/R/library/Cubist/libs/Cubist.so.avx2
/usr/lib64/R/library/Cubist/libs/Cubist.so.avx512
