DROP TABLE if EXISTS MysticCodes;
DROP TABLE if EXISTS servants;
DROP TABLE if EXISTS CraftEssences;

CREATE TABLE MysticCodes (
    mname text,
    description text
);

CREATE TABLE servants (
    name text,
    NP text,
    Rarity text,
    scost int,
    S1 text,
    S2 text,
    S3 text,
    ServantClass text,
    description text
);

CREATE TABLE CraftEssences (
    cname text,
    ccost int,
    crarity text,
    description text
);

insert into servants values ("No Servant", "No NP", "0", "0", "No skills", "No skills", "No skills", "Blank", "cutting costs for the party with this huh?");
insert into servants values ("Arturia", "Excalibur", "5", "16", "Charisma B", "Mana Burst A", "Instinct A", "Saber", "A legendary king of Britain. Also called the King of Knights.");
insert into servants values ("Scathach", "Gae Bolg Alternative", "5", "16", "Wisdom of Dun Scaith A+", "Primeval Rune", "God Slayer B", "Lancer",  "A warrior-queen from Celtic - Ulster mythology.");
insert into servants values ("Gilgamesh", "Enuma Elish", "5", "16", "Charisma A+", "Golden Rule A", "Collector EX", "Archer", "Before the Modern Era, this demigod king governed the Sumerian city-state of Uruk.");
insert into servants values ("Tamamo no Mae", "Eightfold Blessings of Amaterasu", "5", "16", "Witchcraft EX", "Morph A", "Foxs Wedding EX", "Caster", "A good-wife-aspirant, extravagant miko shaman.");
insert into servants values ("Martha", "Tarasque", "4", "12", "Protection of Faith A", "Miracle D+", "Vow of the Saintess C", "Rider", "A holy woman from the 1st Century who appeased the evil dragon Tarasque.");
insert into servants values ("Asterios", "Chaos Labyrinth", "1", "3", "Monstrous Strength A", "Natural Demon A++", "Labrys of the Abyss C", "Berserker", "Asterios - a monster (hero) bestowed with the name of lightning, but he was almost never called by that name.");
insert into servants values ("Ibaraki Douji", "Great Grudge of Rashomon", "4", "12", "Demonic Nature of Oni A", "Disengage A", "Morph A", "Berserker", "During the Heian period, one of the oni that appeared on the imperial capital and exhaustively carried out atrocities.");
insert into servants values ("Mordred", "Clarent Blood Arthur", "5", "16", "Mana Burst A", "Instinct B", "Secret of Pedigree EX", "Saber", "Mordred is a Knight of the Round Table and the legitimate child of King Arthur.");

insert into CraftEssences values ("No CE","0","0","A blank, cutting costs for the party with this huh?");
insert into CraftEssences values ("Kaleidoscope", "12", "5", "Starts battle with 80% NP gauge.");
insert into CraftEssences values ("Divine Banquet", "9", "4", "Increases NP generation rate by 25%.");
insert into CraftEssences values ("The Black Grail", "12", "5", "Increases NP damage by 60%. Loses 500 HP every turn.");
insert into CraftEssences values ("Crown of the Stars", "9", "4", "When equipped on Arturia Pendragon, Increases partys attack by 15% while she is on the field.");
insert into CraftEssences values ("Key of the Kings Law", "9", "4", "When equipped on Gilgamesh, Increases own NP damage by 30%. 30% Chance to increase own critical damage by 10% for 3 turns when attacking.");
insert into CraftEssences values ("Gazing Upon Dun Scaith", "9", "4", "When equipped on Scathach, Increases partys Quick performance by 15% while she is on the field.");
insert into CraftEssences values ("Volumen Hydrargyrum", "12", "5", "Grants Invincibility for 3 attacks. Increases damage by 200.");
insert into CraftEssences values ("The Red Black Keys", "5", "3", "Increases Buster performance by 8%.");
insert into CraftEssences values ("Dragons Meridian", "5", "3", "Starts battle with 30% NP gauge.");
insert into CraftEssences values ("Heavens Feel", "12", "5", "Increases NP damage by 40%.");
insert into CraftEssences values ("Meditation", "1", "1", "Increases debuff resistance by 5%.");

insert into MysticCodes values ("Chaldea", "Base uniform. Comes with healing, evading, and atk up capabilities");
insert into MysticCodes values ("Combat Uniform", "A plugsuit designed around improving combat efficienct");
insert into MysticCodes values ("Mages Association Uniform", "Fitted with healing, NP charge up, and shuffle abilities");
insert into MysticCodes values ("Royal Brand", "This black suit weighs heavily on your shoulders");
insert into MysticCodes values ("Arctic Region Chaldea Uniform", "Designed for exploration in the Arctic Regions where one may experience extreme cold weather");
