%global tl_name formlett
%global tl_revision 21480

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Letters to multiple recipients
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/formlett
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/formlett.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/formlett.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for multiple letters from the same basic source; the package
offers parametrisation of the letters actually sent.

