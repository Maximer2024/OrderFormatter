class OrderFormatter:
    @staticmethod
    def format_order_numbers(input_text: str) -> str:
        order_numbers = input_text.split()
        formatted_string = ", ".join(order_numbers)
        return formatted_string