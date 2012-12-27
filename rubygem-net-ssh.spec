# Generated from net-ssh-2.2.2.gem by gem2rpm -*- rpm-spec -*-
%define rbname net-ssh
%define version 2.2.2
%define release 3

Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/net-ssh/net-ssh
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
#Source1: rubygem-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(net-ssh) = %{version}

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gembuilddir %{buildroot}%{gemdir}

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
%{__rm} -rf %{gembuilddir}/cache

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gemdir}/gems/net-ssh-2.2.2/CHANGELOG.rdoc
%{gemdir}/gems/net-ssh-2.2.2/Manifest
%doc %{gemdir}/gems/net-ssh-2.2.2/README.rdoc
%{gemdir}/gems/net-ssh-2.2.2/Rakefile
%{gemdir}/gems/net-ssh-2.2.2/Rudyfile
%doc %{gemdir}/gems/net-ssh-2.2.2/THANKS.rdoc
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/agent.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/constants.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/key_manager.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/methods/abstract.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/methods/hostbased.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/methods/keyboard_interactive.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/methods/password.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/methods/publickey.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/pageant.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/authentication/session.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/buffer.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/buffered_io.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/config.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/connection/channel.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/connection/constants.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/connection/session.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/connection/term.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/errors.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/key_factory.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/known_hosts.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/loggable.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/packet.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/prompt.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/proxy/command.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/proxy/errors.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/proxy/http.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/proxy/socks4.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/proxy/socks5.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/ruby_compat.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/service/forward.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test/channel.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test/extensions.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test/kex.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test/local_packet.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test/packet.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test/remote_packet.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test/script.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/test/socket.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/algorithms.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/cipher_factory.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/constants.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/hmac.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/hmac/abstract.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/hmac/md5.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/hmac/md5_96.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/hmac/none.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/hmac/sha1.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/hmac/sha1_96.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/identity_cipher.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/kex.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/kex/diffie_hellman_group1_sha1.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/kex/diffie_hellman_group_exchange_sha1.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/openssl.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/packet_stream.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/server_version.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/session.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/transport/state.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/verifiers/lenient.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/verifiers/null.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/verifiers/strict.rb
%{gemdir}/gems/net-ssh-2.2.2/lib/net/ssh/version.rb
%{gemdir}/gems/net-ssh-2.2.2/net-ssh.gemspec
%{gemdir}/gems/net-ssh-2.2.2/setup.rb
%{gemdir}/gems/net-ssh-2.2.2/support/arcfour_check.rb
%{gemdir}/gems/net-ssh-2.2.2/support/ssh_tunnel_bug.rb
%{gemdir}/gems/net-ssh-2.2.2/test/README.txt
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/methods/common.rb
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/methods/test_abstract.rb
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/methods/test_hostbased.rb
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/methods/test_keyboard_interactive.rb
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/methods/test_password.rb
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/methods/test_publickey.rb
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/test_agent.rb
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/test_key_manager.rb
%{gemdir}/gems/net-ssh-2.2.2/test/authentication/test_session.rb
%{gemdir}/gems/net-ssh-2.2.2/test/common.rb
%{gemdir}/gems/net-ssh-2.2.2/test/configs/eqsign
%{gemdir}/gems/net-ssh-2.2.2/test/configs/exact_match
%{gemdir}/gems/net-ssh-2.2.2/test/configs/host_plus
%{gemdir}/gems/net-ssh-2.2.2/test/configs/multihost
%{gemdir}/gems/net-ssh-2.2.2/test/configs/nohost
%{gemdir}/gems/net-ssh-2.2.2/test/configs/numeric_host
%{gemdir}/gems/net-ssh-2.2.2/test/configs/wild_cards
%{gemdir}/gems/net-ssh-2.2.2/test/connection/test_channel.rb
%{gemdir}/gems/net-ssh-2.2.2/test/connection/test_session.rb
%{gemdir}/gems/net-ssh-2.2.2/test/manual/test_forward.rb
%{gemdir}/gems/net-ssh-2.2.2/test/test_all.rb
%{gemdir}/gems/net-ssh-2.2.2/test/test_buffer.rb
%{gemdir}/gems/net-ssh-2.2.2/test/test_buffered_io.rb
%{gemdir}/gems/net-ssh-2.2.2/test/test_config.rb
%{gemdir}/gems/net-ssh-2.2.2/test/test_key_factory.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/hmac/test_md5.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/hmac/test_md5_96.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/hmac/test_none.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/hmac/test_sha1.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/hmac/test_sha1_96.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/kex/test_diffie_hellman_group1_sha1.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/kex/test_diffie_hellman_group_exchange_sha1.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/test_algorithms.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/test_cipher_factory.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/test_hmac.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/test_identity_cipher.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/test_packet_stream.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/test_server_version.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/test_session.rb
%{gemdir}/gems/net-ssh-2.2.2/test/transport/test_state.rb


%doc %{gemdir}/doc/net-ssh-2.2.2
%{gemdir}/cache/net-ssh-2.2.2.gem
%{gemdir}/specifications/net-ssh-2.2.2.gemspec

%changelog
* Thu Dec 27 2012 Sean P. Kane <spkane00@gmail.com> - 2.2.2-3
- Merge

* Tue Sep 18 2012 Sergio Rubio <rubiojr@frameos.org> - 2.2.2-2
- regenerated spec file using gem2rpm

* Mon Sep 17 2012 Sean P. Kane <spkane00@gmail.com> - 2.2.2-1
- Initial version

