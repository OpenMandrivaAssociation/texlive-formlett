# revision 21480
# category Package
# catalog-ctan /macros/generic/formlett
# catalog-date 2010-12-21 20:58:16 +0100
# catalog-license noinfo
# catalog-version 2.3
Name:		texlive-formlett
Version:	2.3
Release:	5
Summary:	Letters to multiple recipients
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/formlett
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formlett.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formlett.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for multiple letters from the same basic source; the
package offers parametrisation of the letters actually sent.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.3-2
+ Revision: 752084
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.3-1
+ Revision: 718494
- texlive-formlett
- texlive-formlett
- texlive-formlett
- texlive-formlett

