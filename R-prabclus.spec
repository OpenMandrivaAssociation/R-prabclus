%global packname  prabclus
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.2.4
Release:          2
Summary:          Clustering of presence-absence, abundance and multilocus genetic data
Group:            Sciences/Mathematics
License:          GPL
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-4.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-MASS R-mclust 
Requires:         R-spdep R-maptools R-foreign R-mvtnorm 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS R-mclust
BuildRequires:    R-spdep R-maptools R-foreign R-mvtnorm 

%description
Distance-based parametric bootstrap tests for clustering with spatial
neighborhood information. Some distance measures, Clustering of
presence-absence, abundance and multilocus genetical data for species
delimitation, nearest neighbor based noise detection. Try package?prabclus
for on overview. Note that the use of the package mclust (called by
function prabclust) is protected by a special license, see
http://www.stat.washington.edu/mclust/license.txt, particularly point 6.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2_2-1
+ Revision: 777738
- Import R-prabclus
- Import R-prabclus

