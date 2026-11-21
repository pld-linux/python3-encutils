#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	encutils
Summary:	Encoding detection collection for Python
Summary(pl.UTF-8):	Zestaw narzędzi do wykrywania kodowania dla Pythona
Name:		python3-%{module}
Version:	1.0.0
Release:	1
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/encutils/
Source0:	https://files.pythonhosted.org/packages/source/e/encutils/%{module}-%{version}.tar.gz
# Source0-md5:	d779b45955179fd3430b92aefc021c8e
URL:		https://github.com/coherent-oss/encutils
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.11
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
BuildRequires:	python3-chardet
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
Conflicts:	python3-cssutils < 2.13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
encutils is a collection of helper functions to detect encodings of
text files (like HTML, XHTML, XML, CSS, etc.) retrieved via HTTP,
file or string. Formerly part of cssutils.

%description -l pl.UTF-8
encutils to zestaw funkcji pomocniczych do wykrywania kodowania
plików tekstowych (HTML, XHTML, XML, CSS itp.) pobranych przez HTTP,
z pliku lub z łańcucha. Wcześniej część cssutils.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
