import logging
import grpc
from mt4grpc.sdk.python3 import mt4_pb2_grpc
from mt4grpc.sdk.python3.mt4_pb2 import *
import configparser
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants (placeholders for sensitive information)
configparser = configparser.ConfigParser()
configparser.read('config.ini')

MT4_SERVER = str(configparser['MT4']['MT4_SERVER'])
USER_ID = int(configparser['MT4']['USER_ID'])
PASSWORD = str(configparser['MT4']['PASSWORD'])
HOST_IP = str(configparser['MT4']['HOST_IP'])

# Establish global variables
channel = None
token = None
trading = None

def connect_to_mt4():
    global channel, token, trading
    """Establish a secure connection with the MT4 server and authenticate."""
    channel = grpc.secure_channel(MT4_SERVER, grpc.ssl_channel_credentials())
    connection = mt4_pb2_grpc.ConnectionStub(channel)
    req = ConnectRequest(user=USER_ID, password=PASSWORD, host=HOST_IP, port=443)
    res = connection.Connect(req)
    if res.error.message:
        logger.error(f"Connection error: {res.error}")
        return None
    trading = mt4_pb2_grpc.TradingStub(channel)
    token = res.result
    logger.info("Connection successful, token: %s", token)
    return token


def account_summary(token):
    """Retrieve account summary using a valid token."""
    mt4 = mt4_pb2_grpc.MT4Stub(channel)
    req = AccountSummaryRequest(id=token)
    res = mt4.AccountSummary(req)
    if res.error.message:
        logger.error("Account summary error: %s", res.error)
        return
    logger.info("Account Summary: %s", res)

def place_order(token, symbol: str, operation: int, volume: float):
    """Place an order on the MT4 platform."""
    trading = mt4_pb2_grpc.TradingStub(channel)
    req = OrderSendRequest(id=token, symbol=symbol, operation=operation, volume=volume)
    res = trading.OrderSend(req)
    if res.error.message:
        logger.error("Order placement error: %s", res.error)
        return
    logger.info("Order placed: %s", res)

def close_all_positions(symbol):
    """Close all positions for a given symbol."""
    open_orders = get_open_orders(symbol)
    for order in open_orders:
        if not close_order(order.Ticket):
            logger.error("Failed to close order with ticket: %s", order.Ticket)
            break  # Stop further closing if an error occurs

def close_order(ticket):
    """Close an individual order."""
    req = OrderCloseRequest(id=token, ticket=ticket)
    res = trading.OrderClose(req)
    if res.error.message:
        logger.error("Error closing order: %s", res.error)
        return False
    logger.info("Order closed: %s", res)
    return True
def get_open_orders(symbol):
    """Retrieve and display open orders for a given symbol."""
    mt4 = mt4_pb2_grpc.MT4Stub(channel)
    req = OpenedOrderRequest(id=token)
    res = mt4.OpenedOrders(req)
    if res.error.message:
        logger.error("Error retrieving open orders: %s", res.error)
        return []
    # Filter orders by symbol
    filtered_orders = [order for order in res.result if order.Symbol == symbol]
    logger.info("Open Orders for %s: %s", symbol, filtered_orders)
    return filtered_orders



if __name__ == "__main__":
    if connect_to_mt4():
        account_summary(token)
        # place_order(token, "BTCUSD", 0, 0.01)
        # get_open_orders("BTCUSD")
        # close_all_positions("BTCUSD")