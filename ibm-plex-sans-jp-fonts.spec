%global fontname ibm-plex-sans-jp
%global fontconf 51-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 6.0.0
Release: 1%{?dist}
Summary: The package of IBM’s typeface, IBM Plex.

License: OFL
URL:     https://github.com/IBM/plex
Source0: https://github.com/IBM/plex/releases/download/v6.0.0/TrueType.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Meet the IBM Plex® typeface, our new corporate typeface family. It’s global, it’s versatile and it’s distinctly IBM.

We designed the IBM Plex typeface carefully to both meet our needs as a global tech company and express who we are as IBMers. It took two years and a lot of work to get here, but today we have a signature typeface we’re proud and excited to share with the world. Discover more about our development of the IBM Plex typeface.

The IBM Plex typeface is an open-source project and available for download and use following the Open Font License (OFL). The IBM Plex family comes in Sans, Serif, Mono and Sans Condensed, all with roman and true italics. The fonts have been designed to work well in user interface (UI) environments, as well as other mediums. This project provides all source files and file formats to support most typographical situations. Currently, IBM Plex Sans supports Extended Latin, Arabic, Cyrillic, Devanagari, Greek, Hebrew, Japanese, Korean and Thai. Chinese will follow in 2022.

Thanks for trying the IBM Plex typeface! We hope you like it.

%prep
%setup -q -n TrueType

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p IBM-Plex-Sans-JP/unhinted/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf
%license IBM-Plex-Sans-JP/unhinted/license.txt

%changelog
* Sat Jan 15 2022 Hideki Tanaka <work@tuxsnct.com> - 6.0.0-1
- Initial packaging.
