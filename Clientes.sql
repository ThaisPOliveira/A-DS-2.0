DROP TABLE IF EXISTS `Clientes`;

CREATE TABLE `Clientes` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `name` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `idade` mediumint default NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Darius Ramirez","a.scelerisque.sed@google.edu",28),
  ("Vance Cameron","eros.non.enim@protonmail.com",20),
  ("Astra Owen","id.ante@icloud.net",70),
  ("Mira Fuller","fusce@google.com",30),
  ("Noah Bryant","morbi.quis@icloud.couk",18),
  ("Chase Gibson","fermentum.fermentum.arcu@hotmail.org",46),
  ("Bevis Molina","tristique@icloud.couk",51),
  ("Wilma Gallagher","enim.etiam@outlook.ca",89),
  ("Desirae Vasquez","nisl.maecenas@aol.couk",62),
  ("Kessie Gregory","lorem.ut@outlook.com",85);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Amity Puckett","libero.proin@outlook.net",82),
  ("Hillary Vaughan","augue.ut@hotmail.edu",84),
  ("Devin Todd","elementum.purus.accumsan@protonmail.ca",49),
  ("Patricia Norman","justo@protonmail.net",41),
  ("Remedios Dominguez","odio.aliquam@yahoo.ca",67),
  ("Graham Craft","cum.sociis@yahoo.couk",53),
  ("Cameron Skinner","mi.lacinia.mattis@icloud.com",22),
  ("Davis Nichols","at.risus@icloud.edu",72),
  ("Kane Wiley","cras.eu.tellus@protonmail.net",57),
  ("Jayme Reeves","convallis.erat@outlook.edu",29);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Germane Guthrie","iaculis.lacus.pede@outlook.org",82),
  ("Aline Brennan","cursus.non@icloud.com",39),
  ("Inez Joyce","ac.mattis.semper@protonmail.net",44),
  ("Brennan Mccormick","ornare.in@google.net",32),
  ("Jelani Gross","aliquam.enim@protonmail.couk",24),
  ("Blaze Rivers","vehicula.et@hotmail.org",53),
  ("Myles Mclaughlin","vitae.mauris.sit@google.couk",25),
  ("Josephine Wooten","dictum.ultricies@hotmail.org",75),
  ("Gemma Roach","consectetuer.mauris.id@yahoo.org",70),
  ("Tad Allen","sollicitudin@hotmail.org",60);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Kamal Pruitt","dui.nec@aol.com",26),
  ("Emma Vargas","euismod.et.commodo@protonmail.net",31),
  ("Thomas Atkins","non@protonmail.edu",69),
  ("Amos Herman","non.bibendum@yahoo.couk",70),
  ("Harrison Jacobs","vitae.velit@outlook.org",25),
  ("Ivor Ramirez","gravida.sagittis@yahoo.org",19),
  ("Gray Smith","quis@outlook.couk",64),
  ("Declan Fischer","sapien.gravida@aol.net",80),
  ("Sonia Lara","aliquam.adipiscing.lobortis@outlook.org",51),
  ("Raven Hickman","non@google.net",38);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Clayton Moss","gravida.non@icloud.couk",59),
  ("Whitney Moreno","interdum.curabitur@yahoo.edu",28),
  ("Yoshio Bean","metus.vitae.velit@yahoo.net",67),
  ("Vernon Rosales","sagittis@hotmail.ca",53),
  ("Magee Brock","auctor.vitae.aliquet@aol.couk",33),
  ("Colorado Franklin","natoque.penatibus.et@protonmail.couk",81),
  ("Jeremy Maynard","justo.praesent@outlook.couk",76),
  ("Cheyenne Weaver","dolor@outlook.couk",30),
  ("Cairo Marshall","enim@icloud.org",24),
  ("Harlan Burnett","pede.sagittis.augue@outlook.couk",73);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Ori Kemp","ornare.lectus@yahoo.com",67),
  ("Miriam Jensen","sit.amet.faucibus@yahoo.edu",48),
  ("Olivia Cline","vel.turpis.aliquam@hotmail.ca",47),
  ("Ifeoma Burke","sodales.elit@aol.couk",67),
  ("Jin Marshall","vel.convallis.in@hotmail.couk",77),
  ("Mia Porter","amet@icloud.com",59),
  ("Bert Callahan","adipiscing.non@aol.couk",76),
  ("Larissa Nguyen","donec.nibh@protonmail.net",52),
  ("Brenda Henson","blandit.congue.in@protonmail.net",21),
  ("Preston Glover","sed.orci@icloud.com",66);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Nicole Marquez","pellentesque.tellus@google.edu",56),
  ("Keegan Morgan","magna.tellus@google.ca",74),
  ("Ria Gamble","ligula.nullam@outlook.couk",42),
  ("Alexander Coffey","consectetuer.mauris@yahoo.edu",80),
  ("Wade Casey","eu.elit.nulla@protonmail.couk",41),
  ("Emi Cameron","posuere.enim@hotmail.com",79),
  ("Aurora Elliott","ac.arcu.nunc@aol.com",58),
  ("August David","magna.suspendisse@outlook.org",74),
  ("Bruce Sanford","vitae@protonmail.couk",27),
  ("Cailin Langley","ligula.aenean.euismod@aol.edu",82);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Brock Murphy","curabitur.vel@icloud.com",46),
  ("Skyler Noel","ipsum.non@google.com",64),
  ("Lev Massey","lorem.vehicula@google.net",85),
  ("Ciara Glass","sed@aol.couk",23),
  ("Quyn Maldonado","convallis.erat.eget@aol.couk",71),
  ("Eugenia Workman","pede.nonummy@yahoo.net",62),
  ("Colette Johns","turpis.aliquam@google.ca",33),
  ("Fleur Pennington","eu.tellus.eu@outlook.ca",44),
  ("Idona Lancaster","aenean.egestas.hendrerit@outlook.edu",87),
  ("Arden Little","quam@aol.couk",68);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("McKenzie Lynn","ut.lacus.nulla@outlook.net",32),
  ("Ezekiel Sargent","lectus@icloud.org",53),
  ("Steel Keller","etiam.ligula.tortor@icloud.ca",42),
  ("Brian Oneal","cursus@aol.org",77),
  ("Reese Gilliam","diam.eu@hotmail.couk",73),
  ("Fuller Fox","enim.consequat@yahoo.net",71),
  ("Prescott Stark","gravida.sagittis.duis@outlook.couk",22),
  ("Kasimir Prince","donec.nibh@google.edu",19),
  ("Clarke Ramirez","sed.est.nunc@google.org",38),
  ("Justin Ferrell","accumsan.neque@yahoo.edu",66);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Herrod Knowles","ac.risus@outlook.ca",64),
  ("Macey Weiss","ipsum@outlook.ca",76),
  ("Callie Whitaker","sem@protonmail.edu",29),
  ("Nell Harper","consectetuer.adipiscing.elit@outlook.ca",76),
  ("Colby Osborn","massa.mauris@icloud.couk",89),
  ("Morgan Charles","fusce.feugiat.lorem@aol.couk",71),
  ("Britanni Thornton","amet.risus.donec@hotmail.net",61),
  ("Shelly Orr","ut@icloud.couk",86),
  ("Elton Byrd","nunc.quis@hotmail.ca",35),
  ("Judah Lawrence","in@outlook.edu",60);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Cynthia Lindsay","sed.turpis@hotmail.couk",73),
  ("Hayes Hayes","magna.nam.ligula@google.org",31),
  ("Madonna Gilliam","elit.dictum@outlook.edu",75),
  ("Evangeline Duncan","sollicitudin.a.malesuada@outlook.ca",65),
  ("Hanae Bray","integer.vulputate.risus@yahoo.com",83),
  ("Travis Alford","placerat@google.org",42),
  ("Gary Clemons","tristique@outlook.net",40),
  ("Deanna Mayer","rutrum@protonmail.ca",51),
  ("McKenzie Lewis","semper.rutrum@google.net",54),
  ("Sarah Mccullough","aliquam@icloud.com",70);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Stephanie Hess","donec.consectetuer@aol.couk",38),
  ("Colette Salas","hendrerit.neque.in@outlook.edu",77),
  ("Veda Livingston","eleifend.cras.sed@protonmail.couk",36),
  ("Lysandra Holcomb","facilisis.non@aol.org",60),
  ("Ori Tate","neque.nullam@hotmail.ca",32),
  ("Aretha Kemp","aenean.egestas.hendrerit@hotmail.edu",22),
  ("Norman Morales","donec.nibh@google.couk",36),
  ("Breanna Hull","arcu.vestibulum.ut@hotmail.ca",61),
  ("Uriah Carter","in.sodales@icloud.ca",89),
  ("Dillon Gibbs","nec@outlook.net",19);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Sara Randolph","arcu.sed@protonmail.ca",43),
  ("Clark Chen","sed.nulla@yahoo.edu",59),
  ("Cassandra Cantu","aliquam.vulputate.ullamcorper@icloud.ca",62),
  ("Zeus Clemons","ad.litora@protonmail.net",83),
  ("Paki Mills","quis@hotmail.couk",85),
  ("Alexander Jordan","mollis@aol.org",78),
  ("Jared Puckett","ut.odio@outlook.net",20),
  ("Dean Orr","ac.eleifend@google.org",52),
  ("Ahmed Cline","neque.nullam@yahoo.ca",21),
  ("Chester Buckner","vulputate@protonmail.couk",42);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Isadora Branch","ullamcorper.nisl@yahoo.couk",23),
  ("Dale Lawrence","dictum.eu@protonmail.net",89),
  ("Thomas Davis","volutpat.nulla@outlook.edu",77),
  ("Grady Holloway","donec.nibh@icloud.com",38),
  ("Chastity Cash","diam.at.pretium@aol.com",48),
  ("Lucius Farmer","tempus.lorem.fringilla@outlook.edu",18),
  ("Emily Booth","sed.neque.sed@google.ca",57),
  ("Elvis Ruiz","justo.nec.ante@protonmail.couk",46),
  ("Allen Fisher","semper.rutrum.fusce@icloud.org",43),
  ("Kenyon Mckee","aliquet.sem@google.com",26);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Mechelle Joyce","lobortis.ultrices@hotmail.com",64),
  ("Colt Neal","sollicitudin@protonmail.net",30),
  ("Fallon Wade","turpis@hotmail.com",77),
  ("Burton Larsen","libero@icloud.couk",34),
  ("Cynthia Bailey","eu.augue@protonmail.edu",48),
  ("Edan Bird","quis@protonmail.couk",84),
  ("Nero Buchanan","etiam.vestibulum.massa@icloud.edu",80),
  ("Belle Holden","elit@hotmail.edu",45),
  ("Jescie Contreras","sem.egestas@yahoo.org",43),
  ("Karleigh Bowen","consectetuer.mauris.id@outlook.net",43);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Harrison Stein","phasellus.in.felis@yahoo.edu",64),
  ("Scott Erickson","vestibulum.ut@protonmail.org",73),
  ("Adele Rios","purus.nullam@outlook.ca",48),
  ("Fallon Clarke","curabitur.sed@aol.org",89),
  ("Darius Dudley","pede.et@icloud.ca",27),
  ("Adara Myers","etiam.ligula@google.couk",58),
  ("Kiayada Mckinney","etiam@hotmail.couk",83),
  ("Chloe Wilcox","elit.elit@yahoo.couk",44),
  ("Tobias Payne","tempor.augue.ac@protonmail.org",36),
  ("Ezekiel Simon","neque.sed.dictum@google.couk",20);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Kane Zamora","est.congue.a@icloud.edu",54),
  ("Georgia Cameron","convallis.erat@google.edu",19),
  ("Upton Dawson","cubilia.curae@aol.couk",69),
  ("Timothy Mathis","non.egestas.a@google.couk",61),
  ("Noble Richardson","morbi.quis@hotmail.org",53),
  ("Norman Mclean","est@protonmail.com",39),
  ("Kelly Flowers","rhoncus.proin@icloud.com",63),
  ("Alea Green","eu.tellus@icloud.org",48),
  ("Heidi Park","vivamus@yahoo.com",57),
  ("Elvis Wise","penatibus.et.magnis@protonmail.edu",23);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Lawrence Potter","tincidunt.nibh@hotmail.com",63),
  ("Alice Wilkerson","fermentum@hotmail.couk",73),
  ("Tarik Benson","sed.pharetra@google.edu",85),
  ("Donna Pollard","phasellus.vitae@aol.org",66),
  ("Hanae Osborn","eros.nec@yahoo.org",50),
  ("Donovan Garrett","augue.scelerisque@yahoo.couk",52),
  ("Carlos Acosta","placerat.augue.sed@google.ca",65),
  ("Tara Dixon","eu@protonmail.com",49),
  ("Kelsey Mays","torquent.per@icloud.ca",59),
  ("Cora Middleton","cras.dictum.ultricies@protonmail.net",65);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Ivan Wright","lacus.quisque.imperdiet@google.net",51),
  ("Kitra Bray","sollicitudin.orci@icloud.org",19),
  ("Kim Barnett","convallis.est@yahoo.edu",85),
  ("Lacy Lester","vulputate.mauris@hotmail.ca",62),
  ("Stella Conley","vulputate.dui@aol.net",32),
  ("Neville Cabrera","maecenas.libero@outlook.com",40),
  ("Troy Petty","eleifend.nec@aol.com",25),
  ("Glenna Chen","per.inceptos.hymenaeos@aol.com",78),
  ("Colin Barron","sed.et@yahoo.com",65),
  ("Nathan Meyer","sem.ut@google.net",61);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Tiger Hanson","scelerisque.neque@google.com",43),
  ("Karen Hernandez","purus.gravida@hotmail.ca",27),
  ("Dean Greene","auctor@protonmail.couk",62),
  ("Melinda Summers","ipsum.ac@google.edu",77),
  ("Shelley Matthews","libero.est.congue@icloud.edu",88),
  ("Neville Joseph","venenatis@icloud.org",33),
  ("Beverly Daugherty","posuere@hotmail.com",72),
  ("Hop Brock","nascetur.ridiculus@yahoo.org",81),
  ("Bryar Leon","ac.ipsum@outlook.com",82),
  ("Ryder Randall","faucibus.leo.in@icloud.com",61);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Gisela Diaz","natoque.penatibus@protonmail.com",31),
  ("Dora Erickson","ligula.aliquam@outlook.com",60),
  ("Hayden Dickerson","nam@aol.org",49),
  ("Kareem Key","tellus.nunc@protonmail.couk",18),
  ("Lucian Parker","interdum.sed@hotmail.edu",34),
  ("Karly Salazar","lectus.rutrum.urna@icloud.ca",82),
  ("Remedios Moses","proin.ultrices@hotmail.org",54),
  ("Rama Bullock","vestibulum.ut@aol.net",64),
  ("Rana Nixon","fringilla.donec@hotmail.ca",27),
  ("Darrel Kidd","mollis.lectus@hotmail.org",82);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Vivian Rasmussen","ultrices.mauris@google.com",70),
  ("Samson Flynn","arcu.et@yahoo.net",58),
  ("Alice Guthrie","sociis.natoque@hotmail.couk",50),
  ("Amy Mccall","donec@hotmail.couk",22),
  ("Yeo Hood","adipiscing.ligula@protonmail.ca",39),
  ("Violet Hyde","arcu.vel@hotmail.com",52),
  ("Raya Palmer","lacus.vestibulum@outlook.ca",33),
  ("Rhoda Battle","curabitur.consequat@yahoo.net",20),
  ("Caleb Robinson","a.enim.suspendisse@icloud.edu",32),
  ("Jameson Burgess","ligula.eu@hotmail.org",19);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Sonia Petty","enim.curabitur.massa@hotmail.com",87),
  ("Harper Bradley","lacinia.vitae@hotmail.org",51),
  ("Eliana Collier","nulla.semper.tellus@outlook.couk",78),
  ("Thomas Saunders","duis.gravida@icloud.edu",90),
  ("Ivana Savage","aenean@protonmail.couk",62),
  ("Emerson Thomas","ut.mi@yahoo.edu",47),
  ("Quinlan Floyd","pede.ultrices@protonmail.com",48),
  ("Sebastian Case","nec.imperdiet@hotmail.ca",41),
  ("Leandra Chan","laoreet.posuere.enim@aol.ca",59),
  ("Ryan Hahn","nisi.magna.sed@protonmail.net",74);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Lysandra Moon","lacinia@icloud.org",47),
  ("Latifah Jacobson","tincidunt@yahoo.net",75),
  ("Aimee Newton","ipsum.primis@yahoo.com",80),
  ("Garth Leonard","suspendisse.sed.dolor@aol.edu",80),
  ("Abraham Hays","euismod.in.dolor@yahoo.couk",65),
  ("Ezekiel Pittman","ligula.eu@icloud.couk",40),
  ("Nyssa Pena","eget.tincidunt@google.net",18),
  ("Callie Ochoa","dapibus.gravida.aliquam@outlook.org",77),
  ("Aphrodite Miller","non.hendrerit@hotmail.net",41),
  ("Darius Hart","eu.odio@icloud.com",30);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Travis Burke","donec.consectetuer@hotmail.com",25),
  ("Gary Slater","feugiat.placerat.velit@icloud.com",39),
  ("Kylynn Finch","lorem@icloud.net",88),
  ("Winter Rodriquez","lorem.ac.risus@google.ca",45),
  ("Marsden Glass","eu@outlook.ca",35),
  ("Deborah Sims","non.sollicitudin@hotmail.org",39),
  ("Patricia Kerr","egestas@hotmail.com",64),
  ("Chancellor Briggs","maecenas.mi.felis@hotmail.org",46),
  ("Stone Solomon","placerat@hotmail.net",72),
  ("Nicole Mills","libero@protonmail.net",67);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Hayden Hines","suscipit@protonmail.org",58),
  ("Elmo Padilla","faucibus.morbi@icloud.net",56),
  ("Zeus Barker","pellentesque@aol.ca",47),
  ("Hanae Hardin","nulla.vulputate.dui@protonmail.org",78),
  ("Bernard Hodges","id.nunc@icloud.couk",54),
  ("Nadine Holder","dictum@yahoo.couk",32),
  ("Fleur Stephens","tincidunt.dui@yahoo.com",45),
  ("Quemby Patel","sociis.natoque@google.edu",20),
  ("Sonia Espinoza","fringilla.purus@google.org",85),
  ("Stewart Spencer","enim.mauris.quis@protonmail.org",77);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Cathleen Nash","blandit.viverra@hotmail.org",84),
  ("Maggie Odom","diam.nunc@outlook.ca",59),
  ("Ima Galloway","metus.aenean@aol.ca",55),
  ("William Lyons","dui.lectus@yahoo.net",25),
  ("Latifah Cotton","condimentum.eget.volutpat@protonmail.net",45),
  ("Elaine White","justo@hotmail.org",28),
  ("Marcia Lloyd","interdum@outlook.net",25),
  ("Helen Stevenson","odio.a@outlook.ca",56),
  ("Candace Macdonald","quis.diam@protonmail.com",40),
  ("Driscoll Levine","faucibus.morbi@yahoo.ca",77);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Ila Bender","sed@protonmail.ca",24),
  ("Graham Thompson","vulputate.risus.a@hotmail.edu",55),
  ("Odessa Campos","odio.a.purus@protonmail.ca",24),
  ("Jesse Bryan","convallis.erat@google.edu",56),
  ("Tatum Maxwell","et.ultrices@aol.couk",59),
  ("Abel Camacho","arcu.vel@icloud.org",71),
  ("Harper Roberson","erat@aol.edu",67),
  ("Neve Perry","nisi@protonmail.org",46),
  ("Aimee Travis","luctus.felis@aol.edu",37),
  ("Quamar White","tincidunt.aliquam@protonmail.ca",25);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Keiko Love","ac.ipsum@yahoo.com",43),
  ("Drake Fry","sapien.aenean.massa@aol.couk",48),
  ("Keaton Le","orci@yahoo.ca",57),
  ("Cullen Allen","quisque@protonmail.org",77),
  ("Hasad Nielsen","facilisis.non@yahoo.edu",55),
  ("Zephr Lowery","donec.est@outlook.ca",73),
  ("Colin Harmon","ullamcorper.velit@hotmail.edu",34),
  ("Imogene Atkins","a.arcu@hotmail.net",51),
  ("Isaac Norton","id.ante@aol.com",73),
  ("Elton Vang","ligula.nullam.feugiat@outlook.couk",78);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Bruce Patterson","nec.cursus@yahoo.org",45),
  ("Edward Williams","amet@aol.net",74),
  ("Briar Bauer","feugiat.non@yahoo.ca",81),
  ("Joshua Bartlett","morbi@hotmail.org",87),
  ("Brenden Howell","nunc@google.edu",31),
  ("Aline Cross","consequat.auctor@hotmail.edu",67),
  ("Tamara Santos","integer.urna.vivamus@aol.ca",78),
  ("Eleanor Mcintyre","nisi.nibh.lacinia@icloud.com",24),
  ("Basia Brewer","purus@aol.net",80),
  ("Brandon Montgomery","magna.cras.convallis@aol.ca",51);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Leo Best","phasellus.dolor@google.couk",70),
  ("Nicole Olsen","elementum.at@aol.org",73),
  ("Dean Dawson","vehicula.risus@icloud.com",21),
  ("Caryn Velazquez","arcu.vestibulum@aol.com",79),
  ("Dante Stewart","dictum@hotmail.edu",21),
  ("Violet Diaz","nascetur.ridiculus@google.couk",38),
  ("Jameson Pollard","odio.sagittis@aol.couk",63),
  ("Malachi Valdez","lacinia.vitae.sodales@icloud.com",69),
  ("Avram Alvarado","ultrices@hotmail.edu",42),
  ("Aileen Freeman","eu@protonmail.couk",76);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Sylvester Glenn","accumsan.interdum@hotmail.ca",90),
  ("Blaze Lloyd","bibendum.donec.felis@aol.ca",68),
  ("Shelley Becker","non@outlook.ca",26),
  ("Nissim Mcdonald","dapibus.quam.quis@outlook.edu",23),
  ("Hashim Hays","aliquam.eros@protonmail.edu",79),
  ("Theodore Velazquez","vel.quam@hotmail.org",35),
  ("Jared Gibbs","eleifend.non.dapibus@yahoo.com",23),
  ("Lydia Callahan","lacus.mauris.non@hotmail.com",78),
  ("Lani Wiggins","in@aol.ca",49),
  ("Jade Roth","massa.mauris@google.org",32);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Kuame Sweet","pede.nec.ante@protonmail.couk",61),
  ("Kelsie Golden","dui@aol.org",35),
  ("Samuel Martin","cum.sociis@aol.net",46),
  ("Isabella Pena","penatibus.et.magnis@aol.ca",60),
  ("Aidan Atkinson","fermentum.arcu.vestibulum@outlook.couk",79),
  ("Ciara Holt","est.tempor@protonmail.com",79),
  ("Karyn Best","nunc.ullamcorper.eu@protonmail.couk",53),
  ("Upton Trevino","nullam.ut@protonmail.org",47),
  ("Aileen Holland","facilisis.lorem@icloud.com",71),
  ("Baxter Mendoza","posuere.cubilia.curae@outlook.com",37);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Curran Horne","integer.vitae@icloud.ca",30),
  ("Nola Mason","in.at.pede@yahoo.net",31),
  ("Allegra Hahn","quam.curabitur@hotmail.com",84),
  ("Helen Hebert","felis.eget@aol.org",23),
  ("Patrick Rutledge","taciti.sociosqu@yahoo.org",23),
  ("Harrison Medina","cras@icloud.edu",45),
  ("Christian Nguyen","orci.phasellus@outlook.com",33),
  ("Xantha Stein","nunc.ullamcorper.eu@outlook.edu",81),
  ("Xavier Gibson","etiam@aol.net",61),
  ("Nigel Dawson","congue@aol.com",42);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Karleigh Chase","a@icloud.ca",36),
  ("Theodore Callahan","donec@google.net",59),
  ("Justin Padilla","a@outlook.ca",21),
  ("Jena Vang","ac.risus@aol.couk",46),
  ("Hammett Chaney","tincidunt.dui@yahoo.ca",63),
  ("Cara Garrison","gravida.non.sollicitudin@yahoo.edu",38),
  ("Sharon Paul","pharetra.ut@outlook.org",44),
  ("Lenore Cohen","posuere@outlook.couk",55),
  ("Ignacia Santiago","gravida.molestie@hotmail.com",63),
  ("Phelan Reese","tincidunt.aliquam@hotmail.com",70);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Guinevere Herman","aliquam.iaculis@yahoo.edu",34),
  ("Otto Gilmore","vitae.semper.egestas@outlook.com",78),
  ("Brynne Hale","neque.nullam@google.couk",58),
  ("Tyrone Stokes","mi.ac@protonmail.ca",78),
  ("Jessica Coleman","natoque.penatibus@protonmail.org",32),
  ("Belle Holden","nec@google.org",55),
  ("Holmes Banks","metus@aol.net",69),
  ("Branden Bright","pede.suspendisse@icloud.ca",26),
  ("Kamal Fry","vivamus.sit@aol.net",77),
  ("Reece Brock","eu@hotmail.ca",55);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Kadeem Wallace","donec.at@aol.org",66),
  ("Serina Avery","augue.ut@google.edu",43),
  ("Tanek Lang","magna.nec.quam@protonmail.couk",37),
  ("Constance Stevenson","convallis@icloud.couk",72),
  ("Giacomo Gonzalez","etiam.bibendum@aol.org",42),
  ("May Robbins","amet.consectetuer@icloud.ca",77),
  ("Darius Craft","ut.aliquam@yahoo.net",48),
  ("Shelley Frederick","dolor@google.edu",44),
  ("Len Bright","ultrices.a@google.com",41),
  ("Fay Clemons","neque.in@hotmail.couk",30);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Herrod Brock","erat.volutpat.nulla@outlook.ca",58),
  ("Thor Flynn","sed.dolor@outlook.ca",45),
  ("Finn Alvarez","ut@protonmail.edu",56),
  ("Dylan Frost","elit.aliquam@yahoo.edu",22),
  ("Haviva Watts","sit.amet@aol.org",64),
  ("Amir Wolfe","nunc@google.couk",76),
  ("Kylan Gould","ridiculus.mus@yahoo.couk",47),
  ("Yardley Hensley","amet.luctus@outlook.ca",86),
  ("Jana Kirk","non.quam@outlook.ca",31),
  ("Kibo Woodward","sit.amet.metus@yahoo.org",18);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Griffith Morales","sodales.at.velit@protonmail.com",28),
  ("Ivy Valdez","fusce.diam@yahoo.ca",79),
  ("Aileen Blevins","arcu.vivamus@icloud.org",28),
  ("Winifred Hebert","sed@aol.com",81),
  ("Karina Santos","tincidunt.vehicula@outlook.ca",19),
  ("Noel Salazar","suspendisse.non@google.com",68),
  ("Fay Singleton","et@hotmail.edu",87),
  ("Ria Wheeler","penatibus.et@protonmail.couk",26),
  ("Hyacinth Morales","neque.sed@protonmail.net",71),
  ("Kiona Daniels","velit@outlook.edu",28);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Wallace Holmes","libero.morbi.accumsan@icloud.org",87),
  ("Karleigh Moon","aliquam@google.couk",39),
  ("Sylvia Cross","per.inceptos.hymenaeos@hotmail.org",80),
  ("Chaim Cooper","nullam.feugiat@hotmail.edu",50),
  ("Orlando Morgan","purus@protonmail.net",62),
  ("Ruby Foley","elementum.sem@outlook.org",32),
  ("Meredith Glenn","consectetuer.adipiscing@protonmail.couk",74),
  ("Judith Love","cursus.a@protonmail.ca",47),
  ("Camille Huffman","vel.pede@outlook.net",80),
  ("Ima Madden","eu.turpis.nulla@aol.edu",78);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Mufutau Valenzuela","parturient@aol.ca",28),
  ("Craig Gates","lectus@hotmail.com",72),
  ("Reese Hughes","id@hotmail.couk",26),
  ("Juliet Swanson","metus@protonmail.org",65),
  ("Christian O'Neill","nunc.sit.amet@yahoo.ca",84),
  ("Veda Johnson","mauris@outlook.edu",56),
  ("Brooke Lopez","ac@protonmail.edu",76),
  ("Matthew Joyner","mi@yahoo.com",77),
  ("Russell Murray","ipsum.dolor@yahoo.edu",83),
  ("Abdul O'Neill","consectetuer.adipiscing@outlook.org",55);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Rae Nichols","aliquam.rutrum.lorem@google.couk",85),
  ("Amity Hogan","lobortis.mauris.suspendisse@icloud.net",37),
  ("Graiden Vance","vivamus@google.org",61),
  ("Buffy Snow","nunc.id.enim@aol.couk",64),
  ("Alyssa Dickerson","fusce.dolor@hotmail.couk",74),
  ("Yasir Ballard","ante@google.com",58),
  ("Mary Jenkins","interdum.ligula@google.org",25),
  ("Nero Witt","fusce.feugiat.lorem@hotmail.couk",27),
  ("Chadwick Fitzgerald","dui.augue@yahoo.net",49),
  ("Troy Walters","auctor.velit@google.edu",73);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Xanthus Acosta","odio.semper@google.couk",55),
  ("Roth Mcintosh","nunc.mauris@yahoo.org",41),
  ("Raphael Warner","phasellus.elit.pede@google.com",52),
  ("Price Burnett","in.consectetuer@protonmail.com",35),
  ("Ashton Graves","pellentesque.massa@yahoo.com",23),
  ("Nero Fields","lacus.cras.interdum@outlook.couk",21),
  ("Jin Peck","elit.dictum.eu@google.edu",50),
  ("Lysandra Gaines","lectus.justo@outlook.com",71),
  ("Rebekah Donovan","magna.a@protonmail.net",80),
  ("Vance Rosario","lorem.fringilla@icloud.com",69);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Shannon Richards","purus.gravida@hotmail.net",55),
  ("Urielle Rocha","cras.dictum@aol.com",20),
  ("Ingrid Merrill","luctus.ut@aol.net",38),
  ("Neil Pate","felis.purus.ac@yahoo.com",76),
  ("Zenia Cantu","in.aliquet@icloud.ca",73),
  ("Noble Holcomb","nulla.interdum.curabitur@hotmail.org",37),
  ("Macy Chapman","magna.et@yahoo.ca",22),
  ("Jasper Morgan","nulla.aliquet.proin@google.net",58),
  ("Patrick Byers","sed.nunc@outlook.ca",32),
  ("Uriel Collier","nunc@aol.ca",30);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Inga Stark","magna.suspendisse@hotmail.edu",38),
  ("Scarlet Key","erat.in@icloud.ca",61),
  ("Rina Carroll","dignissim.maecenas.ornare@hotmail.edu",38),
  ("Germaine Hobbs","sit.amet@icloud.edu",35),
  ("Akeem Valenzuela","proin@icloud.org",62),
  ("Maia Mcintyre","nec.enim@icloud.org",30),
  ("Jacob Everett","sapien@outlook.org",29),
  ("Imani Pope","faucibus.id@icloud.couk",65),
  ("Jaquelyn Peterson","a@hotmail.org",22),
  ("Kim Delgado","tempor.erat.neque@protonmail.couk",63);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Virginia Dunlap","nisl.maecenas@hotmail.edu",62),
  ("Lucas Austin","proin.dolor@aol.net",69),
  ("Vladimir Robinson","diam.luctus.lobortis@yahoo.edu",83),
  ("Iris Walker","sociis@outlook.org",43),
  ("Jason Rodriquez","nec.tempus@google.ca",70),
  ("Keane Crawford","orci.lacus.vestibulum@google.couk",52),
  ("Aquila Ingram","molestie.sed@hotmail.org",29),
  ("Dorian Weiss","nibh.enim@outlook.couk",43),
  ("Norman Parks","et.risus@hotmail.com",57),
  ("Abra Fitzgerald","pretium.neque@protonmail.net",51);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Oscar Velazquez","nec.leo@aol.net",21),
  ("Levi Houston","aliquam.adipiscing.lacus@aol.ca",46),
  ("Amity Robertson","euismod.est@yahoo.org",66),
  ("Aquila Wells","ut@aol.com",53),
  ("Jessica Guerrero","viverra.maecenas@aol.com",69),
  ("Leila Villarreal","sit.amet@outlook.edu",26),
  ("Althea Winters","proin.nisl.sem@hotmail.com",34),
  ("Dai King","orci.sem@yahoo.com",25),
  ("Colton Holder","sed.leo.cras@aol.org",50),
  ("Harlan Fuller","cursus.a@hotmail.ca",44);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Lester Rasmussen","arcu.nunc@outlook.ca",26),
  ("Barbara Chan","est.nunc@google.com",80),
  ("Cora Meyer","eu@google.ca",21),
  ("Portia Phillips","ante@protonmail.ca",45),
  ("Bryar Wilkerson","lorem.ipsum.dolor@outlook.edu",62),
  ("Carter Rodriquez","congue.in@icloud.com",59),
  ("Remedios Hansen","elementum.lorem.ut@outlook.couk",78),
  ("Yeo Ferguson","urna.nullam@outlook.edu",19),
  ("Owen Clarke","amet@outlook.net",28),
  ("Hedy Reid","morbi@hotmail.edu",29);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Josephine Short","orci.lacus@aol.ca",66),
  ("Brenda Soto","est.arcu@outlook.net",83),
  ("Winter Craft","mollis.nec@google.ca",60),
  ("Nehru Burt","orci@protonmail.couk",29),
  ("Zenaida Bauer","metus.facilisis.lorem@google.net",34),
  ("Connor Bennett","vestibulum.neque@aol.com",44),
  ("Dante Sawyer","sodales.elit@icloud.couk",60),
  ("Leo Bridges","euismod.in.dolor@yahoo.ca",22),
  ("Kasper Jensen","lorem.semper@aol.net",39),
  ("Jonah Cohen","mauris.ut@aol.net",27);
INSERT INTO `Clientes` (`name`,`email`,`idade`)
VALUES
  ("Hedda Mack","nulla.facilisis@yahoo.ca",43),
  ("Heidi Weaver","a.arcu.sed@yahoo.couk",35),
  ("Anika Simmons","convallis.erat@google.ca",56),
  ("Hedley Long","sem.ut.cursus@protonmail.edu",32),
  ("Tatyana Browning","lacus.mauris@yahoo.org",23),
  ("Beck Santos","dolor.quam.elementum@icloud.net",64),
  ("Amal Chavez","nulla.vulputate@outlook.ca",30),
  ("Ingrid Head","non.ante@outlook.edu",84),
  ("Dennis Witt","dolor.sit.amet@hotmail.edu",54),
  ("Mark Pugh","penatibus.et@protonmail.org",20);
  
#seleciona as pessoas entre 18 e 20 em ordem crescente
SELECT 
    name, email, idade
FROM
    Clientes
WHERE
    idade >= 18 AND idade <= 20
ORDER BY idade ASC;
 
 select name,email from Clientes limit 30;
 select * from Clientes order by name;
 select * from Clientes where idade >= 40 and idade <= 50 order by idade desc;