# revision 15878
# category Package
# catalog-ctan /fonts/elvish
# catalog-date 2008-04-19 23:11:03 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-elvish
Version:	20080419
Release:	1
Summary:	Fonts for typesetting Tolkien Elvish scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/elvish
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elvish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elvish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle provides fonts for Cirth (cirth.mf, etc.) and for
Tengwar (teng10.mf). The Tengwar fonts are supported by macros
in teng.tex, or by the (better documented) tengtex package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/elvish/cirth.mf
%{_texmfdistdir}/fonts/source/public/elvish/teng10.mf
%{_texmfdistdir}/fonts/source/public/elvish/tengdev.mf
%{_texmfdistdir}/fonts/source/public/elvish/tengmacs.mf
%{_texmfdistdir}/fonts/source/public/elvish/tengmain.mf
%{_texmfdistdir}/fonts/source/public/elvish/tengsecs.mf
%{_texmfdistdir}/fonts/source/public/elvish/tengteht.mf
%{_texmfdistdir}/fonts/tfm/public/elvish/cirth.tfm
%{_texmfdistdir}/fonts/tfm/public/elvish/teng10.tfm
%doc %{_texmfdistdir}/doc/fonts/elvish/README
%doc %{_texmfdistdir}/doc/fonts/elvish/teng.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
