Name:		texlive-formlett
Version:	2.3
Release:	1
Summary:	Letters to multiple recipients
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/formlett
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formlett.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formlett.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A package for multiple letters from the same basic source; the
package offers parametrisation of the letters actually sent.

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
%{_texmfdistdir}/tex/generic/formlett/formlett.sty
%doc %{_texmfdistdir}/doc/generic/formlett/prog_manual.pdf
%doc %{_texmfdistdir}/doc/generic/formlett/prog_manual.tex
%doc %{_texmfdistdir}/doc/generic/formlett/user_manual.pdf
%doc %{_texmfdistdir}/doc/generic/formlett/user_manual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
