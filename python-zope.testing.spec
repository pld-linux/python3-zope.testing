# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	zope.testing
Summary:	Support for different testing frameworks
Summary(pl.UTF-8):	Obsługa różnych szkieletów testowych
Name:		python-%{module}
Version:	3.10.2
Release:	4
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.testing/zope.testing-%{version}.tar.gz
# Source0-md5:	35fc3139992a92a4db13653167fc7be9
URL:		http://www.zope.org/
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
Obsoletes:	Zope-Testing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%description -l pl.UTF-8
Ten pakiet udostępnia wiele szkieletów testowych. Zawiera elastyczne
narzędzie do uruchamiania testów, obsługuje zarówno doctest jak i
unittest.

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet udostępnia wiele szkieletów testowych. Zawiera elastyczne
narzędzie do uruchamiania testów, obsługuje zarówno doctest jak i
unittest.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif


%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install \
	--install-purelib=%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install \
	--install-purelib=%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/testing
%{py_sitedir}/zope.testing-*.egg-info
%{py_sitedir}/zope.testing-*-nspkg.pth

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitedir}//zope/testing
%{py3_sitedir}//zope.testing-*.egg-info
%{py3_sitedir}//zope.testing-*-nspkg.pth
%endif
