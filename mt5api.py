import logging
import grpc
from mt5grpc import mt5_pb2_grpc, mt5_pb2
import configparser

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration settings
config = configparser.ConfigParser()
config.read('config.ini')

MT5_SERVER = config['MT5']['MT5_SERVER']
USER_ID = int(config['MT5']['USER_ID'])
PASSWORD = config['MT5']['PASSWORD']
HOST_IP = config['MT5']['HOST_IP']

# Global variables for grpc services
channel = None
connection = None
trading = None
token = None

def connect_to_mt5():
    global channel, connection, trading, token
    """Establish a secure connection with the MT5 server and authenticate."""
    channel = grpc.secure_channel(MT5_SERVER, grpc.ssl_channel_credentials())
    connection = mt5_pb2_grpc.ConnectionStub(channel)
    trading = mt5_pb2_grpc.TradingStub(channel)
    req = mt5_pb2.ConnectRequest(user=USER_ID, password=PASSWORD, host=HOST_IP, port=443)
    res = connection.Connect(req)
    if res.error.message:
        logger.error(f"Connection error: {res.error}")
        return False
    token = res.result
    logger.info("Connection successful, token: %s", token)
    return True

def account_summary():
    """Retrieve account summary using a valid token."""
    mt5 = mt5_pb2_grpc.MT5Stub(channel)
    req = mt5_pb2.AccountSummaryRequest(id=token)
    res = mt5.AccountSummary(req)
    if res.error.message:
        logger.error("Account summary error: %s", res.error)
        return
    logger.info("Account Summary: %s", res)

def place_order(symbol: str, operation: int, volume: float):
    """Place an order on the MT5 platform."""
    req = mt5_pb2.OrderSendRequest(
        id=token, symbol=symbol, operation=operation, volume=volume,
        price=0, slippage=0, stoploss=0, takeprofit=0, expertID=0,
        stopLimitPrice=0, placedType=0
    )
    res = trading.OrderSend(req)
    if res.error.message:
        logger.error("Order placement error: %s", res.error)
        return
    logger.info("Order placed: %s", res)

def get_open_orders(symbol):
    """Retrieve and display open orders for a given symbol."""
    mt5 = mt5_pb2_grpc.MT5Stub(channel)
    req = mt5_pb2.OpenedOrdersRequest(id=token)
    res = mt5.OpenedOrders(req)
    if res.error.message:
        logger.error("Error retrieving open orders: %s", res.error)
        return []
    filtered_orders = [order for order in res.result if order.Symbol == symbol]
    logger.info("Open Orders for %s: %s", symbol, filtered_orders)
    return filtered_orders

def close_order(ticket):
    """Close an individual order."""
    req = mt5_pb2.OrderCloseRequest(id=token, ticket=ticket)
    res = trading.OrderClose(req)
    if res.error.message:
        logger.error("Error closing order: %s", res.error)
        return False
    logger.info("Order closed: %s", res)
    return True

def close_all_positions(symbol):
    """Close all positions for a given symbol."""
    open_orders = get_open_orders(symbol)
    for order in open_orders:
        if not close_order(order.Ticket):
            logger.error("Failed to close order with ticket: %s", order.Ticket)
            break  # Optional to stop further closing if an error occurs

if __name__ == "__main__":
    if connect_to_mt5():
        # account_summary()
        # place_order("GBPUSD", 0, 0.01)
        get_open_orders("GBPUSD")
        # close_all_positions("GBPUSD")
