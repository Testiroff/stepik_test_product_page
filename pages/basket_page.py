
from .locators import BasePageLocators
from .base_page import BasePage



class BasketPage(BasePage):

    def not_item_in_basket(self):
        assert not self.is_element_present(*BasePageLocators.BASKET_EMPTY), "Basket full" 
        
   
    

