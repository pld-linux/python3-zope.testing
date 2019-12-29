#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	zope.testing
Summary:	Support for different testing frameworks
Summary(pl.UTF-8):	Obsługa różnych szkieletów testowych
Name:		python-%{module}
Version:	4.7
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zope-testing/
Source0:	https://files.pythonhosted.org/packages/source/z/zope.testing/zope.testing-%{version}.tar.gz
# Source0-md5:	13b45a1c9ec987e75a3f9e83b50d22a4
URL:		https://www.zope.org/
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-devel >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
Requires:	python-zope-base
Obsoletes:	Zope-Testing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of testing frameworks. It supports both
doctest and unittest.

%description -l pl.UTF-8
Ten pakiet udostępnia wiele szkieletów testowych. Obsługuje zarówno
doctest jak i unittest.

%package -n python3-%{module}
Summary:	Support for different testing frameworks
Summary(pl.UTF-8):	Obsługa różnych szkieletów testowych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3
Requires:	python3-zope-base

%description -n python3-%{module}
This package provides a number of testing frameworks. It supports both
doctest and unittest.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet udostępnia wiele szkieletów testowych. Obsługuje zarówno
doctest jak i unittest.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install \
	--install-purelib=%{py_sitedir}

%py_postclean
# tests
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/zope/testing/{test_renormalizing,tests}.py*
%endif

%if %{with python3}
%py3_install \
	--install-purelib=%{py3_sitedir}

# tests
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/testing/{test_renormalizing,tests}.py*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py_sitedir}/zope/testing
%{py_sitedir}/zope.testing-%{version}-py*.egg-info
%{py_sitedir}/zope.testing-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py3_sitedir}/zope/testing
%{py3_sitedir}/zope.testing-%{version}-py*.egg-info
%{py3_sitedir}/zope.testing-%{version}-py*-nspkg.pth
%endif
