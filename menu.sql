DROP TABLE IF EXISTS FOOD;
DROP TABLE IF EXISTS INGREDIENTS;
DROP TABLE IF EXISTS RECIPE;

PRAGMA foreign_keys = ON;

CREATE TABLE FOOD(
    name TEXT PRIMARY KEY,
    sides TEXT,
    meal_type TEXT
);

CREATE TABLE INGREDIENTS(
    name TEXT PRIMARY KEY,
    source TEXT
);

CREATE TABLE RECIPE(
    name TEXT,
    ingredients TEXT,
    FOREIGN KEY (name) REFERENCES FOOD(name)
        ON DELETE CASCADE
);

CREATE TRIGGER update_recipe_name
AFTER UPDATE OF name ON FOOD
FOR EACH ROW
BEGIN
    UPDATE RECIPE
    SET name = NEW.name
    WHERE name = OLD.name;
END;

--FOOD
--sides
INSERT INTO FOOD VALUES('potato salad','','');
INSERT INTO FOOD VALUES('chips','','');
INSERT INTO FOOD VALUES('bread rolls','','');
INSERT INTO FOOD VALUES('salad','','');
INSERT INTO FOOD VALUES('mac n cheese','','');
INSERT INTO FOOD VALUES('mashed potatoes','','');
INSERT INTO FOOD VALUES('corn','','');
INSERT INTO FOOD VALUES('green beans','','');
INSERT INTO FOOD VALUES('baked potatoes','','');
INSERT INTO FOOD VALUES('tomato soup','','');
INSERT INTO FOOD VALUES('fries','','');
INSERT INTO FOOD VALUES('mozzarilla sticks','','');
INSERT INTO FOOD VALUES('coleslaw','','');

--breakfasts
INSERT INTO FOOD VALUES('french toast','','breakfast');
INSERT INTO FOOD VALUES('pancakes','','breakfast');
INSERT INTO FOOD VALUES('breakfast pizza','','breakfast');
INSERT INTO FOOD VALUES('eggs and bacon','','breakfast');
INSERT INTO FOOD VALUES('breakfast sandwiches','','breakfast');
INSERT INTO FOOD VALUES('breakfast burritos','','breakfast');
INSERT INTO FOOD VALUES('waffles','','breakfast');

--lunches
INSERT INTO FOOD VALUES('blts','potato salad,chips','lunch');
INSERT INTO FOOD VALUES('chili dogs','mac n cheese','lunch');
INSERT INTO FOOD VALUES('chicken nuggets','mashed potatoes,corn','lunch');
INSERT INTO FOOD VALUES('toasted ravs','green beans','lunch');
INSERT INTO FOOD VALUES('sandwiches','chips','lunch');
INSERT INTO FOOD VALUES('meatball subs','mozzarella sticks','lunch');
INSERT INTO FOOD VALUES('fried shrimp','fries','lunch');

--dinners
INSERT INTO FOOD VALUES('spaghetti and meatballs','bread rolls,salad','dinner');
INSERT INTO FOOD VALUES('beef burrito bar','','dinner');
INSERT INTO FOOD VALUES('pork on a stick','baked potatoes','dinner');
INSERT INTO FOOD VALUES('grilled cheese','tomato soup','dinner');
INSERT INTO FOOD VALUES('burgers','fries','dinner');
INSERT INTO FOOD VALUES('chicken sandwiches','coleslaw','dinner');
INSERT INTO FOOD VALUES('chicken alfredo','bread rolls,salad','dinner');

--RECIPE
--sides
INSERT INTO RECIPE VALUES('potato salad','');
INSERT INTO RECIPE VALUES('chips','');
INSERT INTO RECIPE VALUES('bread rolls','');
INSERT INTO RECIPE VALUES('salad','salad mix');
INSERT INTO RECIPE VALUES('mac n cheese','');
INSERT INTO RECIPE VALUES('mashed potatoes','');
INSERT INTO RECIPE VALUES('corn','');
INSERT INTO RECIPE VALUES('green beans','');
INSERT INTO RECIPE VALUES('baked potatoes','potatoes');
INSERT INTO RECIPE VALUES('tomato soup','');
INSERT INTO RECIPE VALUES('fries','');
INSERT INTO RECIPE VALUES('mozzarilla sticks','');
INSERT INTO RECIPE VALUES('coleslaw','');

--breakfasts
INSERT INTO RECIPE VALUES('french toast','bread,eggs');
INSERT INTO RECIPE VALUES('pancakes','pancake mix');
INSERT INTO RECIPE VALUES('breakfast pizza','');
INSERT INTO RECIPE VALUES('eggs and bacon','eggs,bacon');
INSERT INTO RECIPE VALUES('breakfast sandwiches','');
INSERT INTO RECIPE VALUES('breakfast burritos','');
INSERT INTO RECIPE VALUES('waffles','pancake mix');

--lunches
INSERT INTO RECIPE VALUES('blts','bacon,lettuce,tomato,bread');
INSERT INTO RECIPE VALUES('chili dogs','hot dogs,hot dog buns,chili');
INSERT INTO RECIPE VALUES('chicken nuggets','');
INSERT INTO RECIPE VALUES('toasted ravs','');
INSERT INTO RECIPE VALUES('sandwiches','bread,deli meat,lettuce,tomato,sliced cheese');
INSERT INTO RECIPE VALUES('meatball subs','hot dog buns,meatballs,marinara sauce');
INSERT INTO RECIPE VALUES('fried shrimp','');

--dinners
INSERT INTO RECIPE VALUES('spaghetti and meatballs','spaghetti noodles,meatballs,spaghetti sauce');
INSERT INTO RECIPE VALUES('beef burrito bar','ground beef, tortillas, sour cream, lettuce, shredded cheese');
INSERT INTO RECIPE VALUES('pork on a stick','');
INSERT INTO RECIPE VALUES('grilled cheese','bread,sliced cheese');
INSERT INTO RECIPE VALUES('burgers','burger patties,burger buns,sliced cheese,lettuce,tomato,pickles');
INSERT INTO RECIPE VALUES('chicken sandwiches','chicken filet,burger buns, pickles');
INSERT INTO RECIPE VALUES('chicken alfredo','fettuccine,fajita chicken,alfredo sauce');

--INGREDIENTS
INSERT INTO INGREDIENTS VALUES('alfredo sauce','walmart');
INSERT INTO INGREDIENTS VALUES('bacon','kuna');
INSERT INTO INGREDIENTS VALUES('bread','walmart');
INSERT INTO INGREDIENTS VALUES('burger buns','walmart');
INSERT INTO INGREDIENTS VALUES('burger patties','kuna');
INSERT INTO INGREDIENTS VALUES('chicken filet','kuna');
INSERT INTO INGREDIENTS VALUES('chili','kuna');
INSERT INTO INGREDIENTS VALUES('deli meat','walmart');
INSERT INTO INGREDIENTS VALUES('eggs','kuna');
INSERT INTO INGREDIENTS VALUES('fajita chicken','kuna');
INSERT INTO INGREDIENTS VALUES('fettuccine','walmart');
INSERT INTO INGREDIENTS VALUES('ground beef','walmart');
INSERT INTO INGREDIENTS VALUES('hot dog buns','walmart');
INSERT INTO INGREDIENTS VALUES('hot dogs','kuna');
INSERT INTO INGREDIENTS VALUES('lettuce','walmart');
INSERT INTO INGREDIENTS VALUES('marinara sauce','kuna');
INSERT INTO INGREDIENTS VALUES('meatballs','kuna');
INSERT INTO INGREDIENTS VALUES('pancake mix','walmart');
INSERT INTO INGREDIENTS VALUES('pickles','walmart');
INSERT INTO INGREDIENTS VALUES('potatoes','walmart');
INSERT INTO INGREDIENTS VALUES('salad mix','walmart');
INSERT INTO INGREDIENTS VALUES('shredded cheese','kuna');
INSERT INTO INGREDIENTS VALUES('sliced cheese','walmart');
INSERT INTO INGREDIENTS VALUES('sour cream','walmart');
INSERT INTO INGREDIENTS VALUES('spaghetti noodles','walmart');
INSERT INTO INGREDIENTS VALUES('spaghetti sauce','kuna');
INSERT INTO INGREDIENTS VALUES('tomato','walmart');
INSERT INTO INGREDIENTS VALUES('tortillas','walmart');