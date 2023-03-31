Name:		texlive-modernposter
Version:	47269
Release:	2
Summary:	A modern LaTeX poster theme
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/modernposter
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modernposter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modernposter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class extends the a0poster class in that it adds support
to easily create posters without the need for taking care of
the layout at all. It allows to use \maketitle to generate a
fancy header containing the title information and also provides
macros to position various different types of text boxes in a
two-column layout. The color scheme is inspired by the
metropolis beamer theme.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/modernposter
%doc %{_texmfdistdir}/doc/latex/modernposter

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
