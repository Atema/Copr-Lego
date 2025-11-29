Name:           lego
Version:        4.29.0
Release:        1
Summary:        Let's Encrypt client and ACME library written in Go

License:        MIT
URL:            https://github.com/go-acme/lego/
Source0:        https://github.com/go-acme/lego/releases/download/v%{version}/%{name}_v%{version}_linux_amd64.tar.gz
Source1:        https://github.com/go-acme/lego/releases/download/v%{version}/%{name}_v%{version}_linux_arm64.tar.gz

%description
Lego is a Let's Encrypt client and ACME library written in Go

%prep
%ifarch x86_64
%define source 0
%endif
%ifarch aarch64
%define source 1
%endif
%setup -q -c -T -a %{source}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc CHANGELOG.md