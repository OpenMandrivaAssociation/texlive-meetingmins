Name:		texlive-meetingmins
Version:	31878
Release:	2
Summary:	Format written minutes of meetings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/meetingmins
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/meetingmins.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/meetingmins.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/meetingmins.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class allows formatting of meeting minutes using \section
commands (which provide hierarchical structure). An agenda can
also be produced for distribution prior to the meeting, with
user-selected portions suppressed from printing.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/meetingmins/meetingmins.cls
%doc %{_texmfdistdir}/doc/latex/meetingmins/README
%doc %{_texmfdistdir}/doc/latex/meetingmins/meetingmins.pdf
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/agenda.pdf
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/agenda.tex
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/chair.pdf
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/chair.tex
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/department.min
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/minutes.pdf
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/minutes.tex
#- source
%doc %{_texmfdistdir}/source/latex/meetingmins/meetingmins.dtx
%doc %{_texmfdistdir}/source/latex/meetingmins/meetingmins.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
