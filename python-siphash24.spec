%define module siphash24

Name:		python-siphash24
Version:	1.9
Release:	1
Summary:	Streaming-capable SipHash-1-3 and SipHash-2-4 Implementation
License:	Apache-2.0 OR LGPL-2.1-or-later
Group:		Development/Python
URL:		https://pypi.org/project/siphash24/
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig(python3)
#BuildRequires:	pkgconfig(libcstdaux-1)
BuildRequires:	pkgconfig(libcsiphash-1)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(meson-python)

%description
Streaming-capable SipHash-1-3 and SipHash-2-4 Implementation.

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
%{__python} -m unittest discover -v

%files
%doc README.rst
%license LICENSES/*
%{python_sitearch}/%{module}.cpython*.so
%{python_sitearch}/%{module}-%{version}.dist-info
