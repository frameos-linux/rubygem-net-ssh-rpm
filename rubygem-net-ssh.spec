%global gem_name net-ssh
%global rubyabi 1.8.7

Summary: Interact with processes on remote servers via SSH2
Name: rubygem-%{gem_name}
Version: 2.2.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://net-ssh.github.com/net-ssh/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby 
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}

%changelog
* Tue Sep 11 2012 Sean P. Kane <spkane00@gmail.com> - 2.2.2-1
- Initial package

