#table table
INSERT INTO `ftserve`.`tables` (`table_ID`, `code`) VALUES ('001', 'asd');
INSERT INTO `ftserve`.`tables` (`table_ID`, `code`) VALUES ('002', 'asd');cutomers
INSERT INTO `ftserve`.`tables` (`table_ID`, `code`) VALUES ('003', 'asd');

#customer
INSERT INTO `ftserve`.`cutomers` (`customer_ID`, `table_ID`, `status`, `timestamp`) VALUES ('1', '1', 'AC', '2021-06-12 21:53:00');
INSERT INTO `ftserve`.`cutomers` (`customer_ID`, `table_ID`, `status`, `timestamp`) VALUES ('2', '2', 'AC', '2021-06-12 21:53:00');
INSERT INTO `ftserve`.`cutomers` (`customer_ID`, `table_ID`, `status`, `timestamp`) VALUES ('3', '3', 'AC', '2021-06-12 22:53:00');

#items
INSERT INTO `ftserve`.`items` (`item_ID`, `name`, `price`, `category`, `staus`, `image_url`, `description`) VALUES ('1', 'Mash Peper Fry', '120.00', 'starter', 'AV', '/static/images/items/sample.jpg', 'Mushroom Pepper Fry Recipe | Crispy Mushroom Salt & Pepper Dry | Mushroom Recipes ');
INSERT INTO `ftserve`.`items` (`item_ID`, `name`, `price`, `category`, `staus`, `image_url`, `description`) VALUES ('2', 'Paneer 65', '120', 'starter', 'AV', '/static/images/items/sample.jpg', ' Paneer 65 is a spicy Hyderabadi appetizer made with paneer, flour, yogurt, curry leaves and spices.');
INSERT INTO `ftserve`.`items` (`item_ID`, `name`, `price`, `category`, `staus`, `image_url`, `description`) VALUES ('3', 'Gobi 65', '100', 'starter', 'AV', '/static/images/items/sample.jpg', 'Gobi 65 is a south Indian snack made of fried cauliflower, spices and herbs.');
INSERT INTO `ftserve`.`items` (`item_ID`, `name`, `price`, `category`, `staus`, `image_url`, `description`) VALUES ('4', 'Carrot Juice', '60', 'Beverages', 'AV', '/static/images/items/sample.jpg', 'Carrot juice is incredibly nutritious, providing potassium, several carotenoids, and vitamins A, C, and K .');
INSERT INTO `ftserve`.`items` (`item_ID`, `name`, `price`, `category`, `staus`, `image_url`, `description`) VALUES ('5', 'Mint Lime Juice', '30', 'Beverages', 'AV', '/static/images/items/sample.jpg', 'This Mint Lime is a fresh squeezed juice of mint and lemon to beat the hot days.');