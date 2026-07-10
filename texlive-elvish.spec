%global tl_name elvish
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts for typesetting Tolkien Elvish scripts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/elvish
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elvish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elvish.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides fonts for Cirth (cirth.mf, etc.) and for Tengwar
(teng10.mf). The Tengwar fonts are supported by macros in teng.tex, or
by the (better documented) tengtex package.

