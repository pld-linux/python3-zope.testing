#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define	module	zope.testing
Summary:	Support for different testing frameworks
Summary(pl.UTF-8):	Obsługa różnych szkieletów testowych
Name:		python3-%{module}
Version:	5.1
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zope-testing/
Source0:	https://files.pythonhosted.org/packages/source/z/zope.testing/zope_testing-%{version}.tar.gz
# Source0-md5:	c431453beaca9914aa10a7dabd79c59e
URL:		https://www.zope.org/
BuildRequires:	python3-devel >= 1:3.9
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.testrunner
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-repoze.sphinx.autointerface
BuildRequires:	python3-zope.exceptions
BuildRequires:	python3-zope.interface
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.9
Requires:	python3-zope-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of testing frameworks. It supports both
doctest and unittest.

%description -l pl.UTF-8
Ten pakiet udostępnia wiele szkieletów testowych. Obsługuje zarówno
doctest jak i unittest.

%package apidocs
Summary:	API documentation for Python zope.testing module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona zope.testing
Group:		Documentation

%description apidocs
API documentation for Python zope.testing module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona zope.testing.

%prep
%setup -q -n zope_testing-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
zope-testrunner-3 --test-path=src
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

# tests for zope.testing itself
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/zope/testing/tests.py \
	$RPM_BUILD_ROOT%{py3_sitescriptdir}/zope/testing/__pycache__/tests.*.py*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/zope/testing
%{py3_sitescriptdir}/zope.testing-%{version}-py*.egg-info
%{py3_sitescriptdir}/zope.testing-%{version}-py*-nspkg.pth

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,api,*.html,*.js}
%endif
