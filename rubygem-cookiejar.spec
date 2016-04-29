#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-cookiejar
Version  : 0.3.3
Release  : 7
URL      : https://rubygems.org/downloads/cookiejar-0.3.3.gem
Source0  : https://rubygems.org/downloads/cookiejar-0.3.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-rubygems-tasks

%description
Ruby CookieJar
==============
**Git**:	[http://github.com/dwaite/cookiejar](http://github.com/dwaite/cookiejar)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n cookiejar-0.3.3
gem spec %{SOURCE0} -l --ruby > rubygem-cookiejar.gemspec

%build
gem build rubygem-cookiejar.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
cookiejar-0.3.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/cookiejar-0.3.3
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/cookiejar-0.3.3.gem
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/README.markdown
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/contributors.json
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/cookiejar.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/lib/cookiejar.rb
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/lib/cookiejar/cookie.rb
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/lib/cookiejar/cookie_validation.rb
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/lib/cookiejar/jar.rb
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/lib/cookiejar/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/spec/cookie_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/spec/cookie_validation_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/spec/jar_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cookiejar-0.3.3/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/cookiejar-0.3.3.gemspec
