DROP TABLE if EXISTS MysticCodes;
DROP TABLE if EXISTS servants;

CREATE TABLE MysticCodes (
    name text,
    description text
);

CREATE TABLE servants (
    name text,
    NP text,
    Rarity text,
    S1 text,
    S2 text,
    S3 text,
    ServantClass text,
    description text
);


insert into servants values ("Arturia", "Excalibur", "5", "Charisma B", "Mana Burst A", "Instinct A", "Saber", "A legendary king of Britain. Also called the King of Knights.");
insert into servants values ("Scathach", "Gae Bolg Alternative", "5", "Wisdom of Dun Scaith A+", "Primeval Rune", "God Slayer B", "Lancer",  "A warrior-queen from Celtic - Ulster mythology.");
insert into servants values ("Gilgamesh", "Enuma Elish", "5", "Charisma A+", "Golden Rule A", "Collector EX", "Archer", "Before the Modern Era, this demigod king governed the Sumerian city-state of Uruk.");
insert into servants values ("Tamamo no Mae", "Eightfold Blessings of Amaterasu", "5", "Witchcraft EX", "Morph A", "Fox's Wedding EX", "Caster", "A good-wife-aspirant, extravagant miko shaman.");
insert into servants values ("Martha", "Tarasque", "4", "Protection of Faith A", "Miracle D+", "Vow of the Saintess C", "Rider", "A holy woman from the 1st Century who appeased the evil dragon Tarasque.");
insert into servants values ("Asterios", "Chaos Labyrinth", "1", "Monstrous Strength A", "Natural Demon A++", "Labrys of the Abyss C", "Berserker", "Asterios - a monster (hero) bestowed with the name of lightning, but he was almost never called by that name.");
insert into servants values ("Ibaraki Douji", "Great Grudge of Rashomon", "4", "Demonic Nature of Oni A", "Disengage A", "Morph A", "Berserker", "During the Heian period, one of the oni that appeared on the imperial capital and exhaustively carried out atrocities.");
insert into servants values ("Mordred", "Clarent Blood Arthur", "5", "Mana Burst A", "Instinct B", "Secret of Pedigree EX", "Saber", "Mordred is a Knight of the Round Table and the legitimate child of King Arthur.");

insert into MysticCodes values ("Chaldea", "Base uniform. Comes with healing, evading, and atk up capabilities");
insert into MysticCodes values ("Combat Uniform", "A plugsuit designed around improving combat efficienct");
insert into MysticCodes values ("Mage's Association Uniform", "Fitted with healing, NP charge up, and shuffle abilities");
insert into MysticCodes values ("Royal Brand", "This black suit weighs heavily on your shoulders");
insert into MysticCodes values ("Arctic Region Chaldea Uniform", "Designed for exploration in the Arctic Regions where one may experience extreme cold weather");
