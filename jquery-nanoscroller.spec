%define		plugin	nanoscroller
Summary:	jQuery nanoScroller plugin
Name:		jquery-%{plugin}
Version:	0.7.2
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/jamesflorentino/nanoScrollerJS/archive/%{version}.tar.gz
# Source0-md5:	ccb6a2580afdbc0a7793c4d29506fc85
URL:		http://jamesflorentino.github.io/nanoScrollerJS/
BuildRequires:	rpmbuild(macros) > 1.268
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
nanoScroller.js is a jQuery plugin that offers a simplistic way of
implementing Mac OS X Lion-styled scrollbars for your website. It uses
minimal HTML markup being .nano > .content. The other scrollbar div
elements .pane > .slider are added during run time to prevent clutter
in templating. The latest version utilizes native scrolling and works
with the iPad, iPhone, and some Android Tablets.

%prep
%setup -qn nanoScrollerJS-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cd bin
cp -p javascripts/jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p javascripts/jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
cp -a css/nanoscroller.css $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE-MIT
%{_appdir}
