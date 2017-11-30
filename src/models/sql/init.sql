drop table if exists entries;
create table entries (
    ID INTEGER PRIMARY KEY autoincrement,
    title string not null,
    text string not null
)