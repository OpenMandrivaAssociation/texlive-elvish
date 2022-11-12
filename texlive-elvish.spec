Name:		texlive-elvish
Version:	15878
Release:	1
Summary:	Fonts for typesetting Tolkien Elvish scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/elvish
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elvish.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elvish.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides fonts for Cirth (cirth.mf, etc.) and for
Tengwar (teng10.mf). The Tengwar fonts are supported by macros
in teng.tex, or by the (better documented) tengtex package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/elvish
%{_texmfdistdir}/fonts/tfm/public/elvish
%doc %{_texmfdistdir}/doc/fonts/elvish

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
