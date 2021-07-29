/* c1.c - Basic Curses Example */

#include <curses.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
    int row, col, k;    
// Create a curses object and define color pairs
    initscr();
    getmaxyx(stdscr,row,col);
    start_color();
    init_pair(1,COLOR_RED,COLOR_WHITE);
    init_pair(2,COLOR_GREEN,COLOR_BLACK);
    init_pair(3,COLOR_WHITE,COLOR_BLUE);
    curs_set(0);
    noecho();
    nodelay(stdscr, TRUE);
// Write a header and footer, first write colored strip, then write text
    bkgd(COLOR_PAIR(3));
    attron(COLOR_PAIR(1));
// Create a top and bottom color strip
    for (int i = 0; i < col; i++) {
        mvaddstr(0, i,  " ");
        mvaddstr(row-1, i,  " ");
    }
    mvaddstr(0, 0,  " Curses C Dynamic Text Example");
    mvaddstr(row-1, 0,  " Key Commands: q - to quit");
    attroff(COLOR_PAIR(1));   
    mvaddstr(2, 5,"RASPBERRY PI SIMULATED SENSOR VALUES" );
    refresh();
// Cycle with new values every 2 seconds until a q key (133) is entered    
    while (k != 113)
    {
        attroff(COLOR_PAIR(2));
        for (int i = 0; i < 10; i++) {
            mvprintw((4+i), 5,  " Sensor %d : ",i);
        }
        attron(COLOR_PAIR(2));
        for (int i = 0; i < 10; i++) {
            mvprintw((4+i), 20,  "%d",rand() %100);
        }
        k = getch();
        sleep(2);
    }
    endwin();
    exit(0);
}
