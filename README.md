Prostředí
---------

Projekt byl vyvíjen na (a pro) Windows 64bit. Při vývoji jsme používali WSL, což nám umožňovalo práci s Linuxovým
terminálem (proto je Makefile psán pro Linux, i když instalační program je vytvořen pro Windows).


Autoři
------

Název týmu: monkaIVS
- xhlins01 Martin Hlinský 
- xdudov02 Petra Dudová 
- xnekul04 Štěpán Nekula 
- xkundr07 Jan Kundrata 

Licence
-------

Tento program je poskytován pod licencí [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

Spuštění projektu
-------

Projekt se dá na Linuxu spustit přes Makefile (příkaz `make`), nebo přímý zápis typu `python3 gui.py`,
`python3 profiling.py`, nebo `python3 mathlibtests.py`.

Na Windows se dá projekt spustit přes přímý zápis stejného typu, ale kvůli rozdílům v příkazech ve Windows
 a Linux prostředí nelze projekt spouštět přes `make` (Je možné ve WSL, ale uživatel si musí nastavit proměnnou DISPLAY
pomocí příkazu typu:

`export DISPLAY=$(echo $(grep nameserver /etc/resolv.conf | sed 's/nameserver //'):0)`).

Pro jednoduchost je pro Windows uživatele vytvořen instalační balíček, pomocí kterého si může program nainstalovat bez
jakékoliv práce s příkazovým řádkem.