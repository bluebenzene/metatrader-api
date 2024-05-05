"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import mt4_pb2 as mt4__pb2

class ConnectionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Connect = channel.unary_unary('/mt4grpc.Connection/Connect', request_serializer=mt4__pb2.ConnectRequest.SerializeToString, response_deserializer=mt4__pb2.ConnectReply.FromString)
        self.CheckConnect = channel.unary_unary('/mt4grpc.Connection/CheckConnect', request_serializer=mt4__pb2.CheckConnectRequest.SerializeToString, response_deserializer=mt4__pb2.CheckConnectReply.FromString)
        self.Disconnect = channel.unary_unary('/mt4grpc.Connection/Disconnect', request_serializer=mt4__pb2.DisconnectRequest.SerializeToString, response_deserializer=mt4__pb2.DisconnectReply.FromString)

class ConnectionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Connect(self, request, context):
        """Connect to account with user, password, host, port.
        <br> [Example] <br>
        { <br>
        "user": "500476959", <br>
        "password": "ehj4bod", <br>
        "host": "mt4-demo.roboforex.com", <br>
        "port": "443" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckConnect(self, request, context):
        """Check connection state and reconnect if connection lost
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Disconnect from account
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ConnectionServicer_to_server(servicer, server):
    rpc_method_handlers = {'Connect': grpc.unary_unary_rpc_method_handler(servicer.Connect, request_deserializer=mt4__pb2.ConnectRequest.FromString, response_serializer=mt4__pb2.ConnectReply.SerializeToString), 'CheckConnect': grpc.unary_unary_rpc_method_handler(servicer.CheckConnect, request_deserializer=mt4__pb2.CheckConnectRequest.FromString, response_serializer=mt4__pb2.CheckConnectReply.SerializeToString), 'Disconnect': grpc.unary_unary_rpc_method_handler(servicer.Disconnect, request_deserializer=mt4__pb2.DisconnectRequest.FromString, response_serializer=mt4__pb2.DisconnectReply.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('mt4grpc.Connection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Connection(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Connect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Connection/Connect', mt4__pb2.ConnectRequest.SerializeToString, mt4__pb2.ConnectReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckConnect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Connection/CheckConnect', mt4__pb2.CheckConnectRequest.SerializeToString, mt4__pb2.CheckConnectReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Connection/Disconnect', mt4__pb2.DisconnectRequest.SerializeToString, mt4__pb2.DisconnectReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class MT4Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AccountSummary = channel.unary_unary('/mt4grpc.MT4/AccountSummary', request_serializer=mt4__pb2.AccountSummaryRequest.SerializeToString, response_deserializer=mt4__pb2.AccountSummaryReply.FromString)
        self.Groups = channel.unary_unary('/mt4grpc.MT4/Groups', request_serializer=mt4__pb2.GroupsRequest.SerializeToString, response_deserializer=mt4__pb2.GroupsReply.FromString)
        self.Quote = channel.unary_unary('/mt4grpc.MT4/Quote', request_serializer=mt4__pb2.QuoteRequest.SerializeToString, response_deserializer=mt4__pb2.QuoteReply.FromString)
        self.OpenedOrders = channel.unary_unary('/mt4grpc.MT4/OpenedOrders', request_serializer=mt4__pb2.OpenedOrdersRequest.SerializeToString, response_deserializer=mt4__pb2.OpenedOrdersReply.FromString)
        self.Symbols = channel.unary_unary('/mt4grpc.MT4/Symbols', request_serializer=mt4__pb2.SymbolsRequest.SerializeToString, response_deserializer=mt4__pb2.SymbolsReply.FromString)
        self.SymbolParams = channel.unary_unary('/mt4grpc.MT4/SymbolParams', request_serializer=mt4__pb2.SymbolParamsRequest.SerializeToString, response_deserializer=mt4__pb2.SymbolParamsReply.FromString)
        self.ServerTimezone = channel.unary_unary('/mt4grpc.MT4/ServerTimezone', request_serializer=mt4__pb2.ServerTimezoneRequest.SerializeToString, response_deserializer=mt4__pb2.ServerTimezoneReply.FromString)
        self.SymbolParamsMany = channel.unary_unary('/mt4grpc.MT4/SymbolParamsMany', request_serializer=mt4__pb2.SymbolParamsManyRequest.SerializeToString, response_deserializer=mt4__pb2.SymbolParamsManyReply.FromString)
        self.OpenedOrder = channel.unary_unary('/mt4grpc.MT4/OpenedOrder', request_serializer=mt4__pb2.OpenedOrderRequest.SerializeToString, response_deserializer=mt4__pb2.OpenedOrderReply.FromString)
        self.OrderHistory = channel.unary_unary('/mt4grpc.MT4/OrderHistory', request_serializer=mt4__pb2.OrderHistoryRequest.SerializeToString, response_deserializer=mt4__pb2.OrderHistoryReply.FromString)
        self.QuoteHistory = channel.unary_unary('/mt4grpc.MT4/QuoteHistory', request_serializer=mt4__pb2.QuoteHistoryRequest.SerializeToString, response_deserializer=mt4__pb2.QuoteHistoryReply.FromString)
        self.QuoteHistoryMany = channel.unary_unary('/mt4grpc.MT4/QuoteHistoryMany', request_serializer=mt4__pb2.QuoteHistoryManyRequest.SerializeToString, response_deserializer=mt4__pb2.QuoteHistoryManyReply.FromString)
        self.ClosedOrders = channel.unary_unary('/mt4grpc.MT4/ClosedOrders', request_serializer=mt4__pb2.ClosedOrdersRequest.SerializeToString, response_deserializer=mt4__pb2.ClosedOrdersReply.FromString)
        self.RequestQuoteHistory = channel.unary_unary('/mt4grpc.MT4/RequestQuoteHistory', request_serializer=mt4__pb2.RequestQuoteHistoryRequest.SerializeToString, response_deserializer=mt4__pb2.RequestQuoteHistoryReply.FromString)
        self.SetPlacedType = channel.unary_unary('/mt4grpc.MT4/SetPlacedType', request_serializer=mt4__pb2.SetPlacedTypeRequest.SerializeToString, response_deserializer=mt4__pb2.SetPlacedTypeReply.FromString)
        self.IsInvestor = channel.unary_unary('/mt4grpc.MT4/IsInvestor', request_serializer=mt4__pb2.IsInvestorRequest.SerializeToString, response_deserializer=mt4__pb2.IsInvestorReply.FromString)

class MT4Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def AccountSummary(self, request, context):
        """Balance, Equity, Currency, FreeMargin, Margin, MarginLevel, Profit, Leverage, Credit
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Groups(self, request, context):
        """Full infromation about symbol groups
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Quote(self, request, context):
        """Get quote
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "symbol": "EURUSD" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenedOrders(self, request, context):
        """List of opened orders
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Symbols(self, request, context):
        """List of symbols.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SymbolParams(self, request, context):
        """Full infromation about symbol and his group
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "symbol": "EURUSD" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerTimezone(self, request, context):
        """Server timezone.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SymbolParamsMany(self, request, context):
        """Full infromation about symbols
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenedOrder(self, request, context):
        """List of opened orders
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "ticket": "0" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderHistory(self, request, context):
        """Order history
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "from": "2022-01-01T00:00:00", <br>
        "to": "2023-06-01T00:00:00" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuoteHistory(self, request, context):
        """Price history.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "symbol": "EURUSD", <br>
        "timeframe": "D1", <br>
        "from": "2022-10-01T00:00:00", <br>
        "count": "10" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuoteHistoryMany(self, request, context):
        """Price history.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "timeframe": "D1", <br>
        "from": "2022-10-01T00:00:00", <br>
        "count": "10" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClosedOrders(self, request, context):
        """Last 10 orders that were closed during current session
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestQuoteHistory(self, request, context):
        """Request price history and get result via /events socket connection
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "symbol": "EURUSD", <br>
        "timeframe": "D1", <br>
        "from": "2022-10-01T00:00:00", <br>
        "count": "10" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPlacedType(self, request, context):
        """Subscribe for order profit updates and get results via /events socket connection
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "type": "Client" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsInvestor(self, request, context):
        """Check investor mode.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MT4Servicer_to_server(servicer, server):
    rpc_method_handlers = {'AccountSummary': grpc.unary_unary_rpc_method_handler(servicer.AccountSummary, request_deserializer=mt4__pb2.AccountSummaryRequest.FromString, response_serializer=mt4__pb2.AccountSummaryReply.SerializeToString), 'Groups': grpc.unary_unary_rpc_method_handler(servicer.Groups, request_deserializer=mt4__pb2.GroupsRequest.FromString, response_serializer=mt4__pb2.GroupsReply.SerializeToString), 'Quote': grpc.unary_unary_rpc_method_handler(servicer.Quote, request_deserializer=mt4__pb2.QuoteRequest.FromString, response_serializer=mt4__pb2.QuoteReply.SerializeToString), 'OpenedOrders': grpc.unary_unary_rpc_method_handler(servicer.OpenedOrders, request_deserializer=mt4__pb2.OpenedOrdersRequest.FromString, response_serializer=mt4__pb2.OpenedOrdersReply.SerializeToString), 'Symbols': grpc.unary_unary_rpc_method_handler(servicer.Symbols, request_deserializer=mt4__pb2.SymbolsRequest.FromString, response_serializer=mt4__pb2.SymbolsReply.SerializeToString), 'SymbolParams': grpc.unary_unary_rpc_method_handler(servicer.SymbolParams, request_deserializer=mt4__pb2.SymbolParamsRequest.FromString, response_serializer=mt4__pb2.SymbolParamsReply.SerializeToString), 'ServerTimezone': grpc.unary_unary_rpc_method_handler(servicer.ServerTimezone, request_deserializer=mt4__pb2.ServerTimezoneRequest.FromString, response_serializer=mt4__pb2.ServerTimezoneReply.SerializeToString), 'SymbolParamsMany': grpc.unary_unary_rpc_method_handler(servicer.SymbolParamsMany, request_deserializer=mt4__pb2.SymbolParamsManyRequest.FromString, response_serializer=mt4__pb2.SymbolParamsManyReply.SerializeToString), 'OpenedOrder': grpc.unary_unary_rpc_method_handler(servicer.OpenedOrder, request_deserializer=mt4__pb2.OpenedOrderRequest.FromString, response_serializer=mt4__pb2.OpenedOrderReply.SerializeToString), 'OrderHistory': grpc.unary_unary_rpc_method_handler(servicer.OrderHistory, request_deserializer=mt4__pb2.OrderHistoryRequest.FromString, response_serializer=mt4__pb2.OrderHistoryReply.SerializeToString), 'QuoteHistory': grpc.unary_unary_rpc_method_handler(servicer.QuoteHistory, request_deserializer=mt4__pb2.QuoteHistoryRequest.FromString, response_serializer=mt4__pb2.QuoteHistoryReply.SerializeToString), 'QuoteHistoryMany': grpc.unary_unary_rpc_method_handler(servicer.QuoteHistoryMany, request_deserializer=mt4__pb2.QuoteHistoryManyRequest.FromString, response_serializer=mt4__pb2.QuoteHistoryManyReply.SerializeToString), 'ClosedOrders': grpc.unary_unary_rpc_method_handler(servicer.ClosedOrders, request_deserializer=mt4__pb2.ClosedOrdersRequest.FromString, response_serializer=mt4__pb2.ClosedOrdersReply.SerializeToString), 'RequestQuoteHistory': grpc.unary_unary_rpc_method_handler(servicer.RequestQuoteHistory, request_deserializer=mt4__pb2.RequestQuoteHistoryRequest.FromString, response_serializer=mt4__pb2.RequestQuoteHistoryReply.SerializeToString), 'SetPlacedType': grpc.unary_unary_rpc_method_handler(servicer.SetPlacedType, request_deserializer=mt4__pb2.SetPlacedTypeRequest.FromString, response_serializer=mt4__pb2.SetPlacedTypeReply.SerializeToString), 'IsInvestor': grpc.unary_unary_rpc_method_handler(servicer.IsInvestor, request_deserializer=mt4__pb2.IsInvestorRequest.FromString, response_serializer=mt4__pb2.IsInvestorReply.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('mt4grpc.MT4', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MT4(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AccountSummary(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/AccountSummary', mt4__pb2.AccountSummaryRequest.SerializeToString, mt4__pb2.AccountSummaryReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Groups(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/Groups', mt4__pb2.GroupsRequest.SerializeToString, mt4__pb2.GroupsReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Quote(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/Quote', mt4__pb2.QuoteRequest.SerializeToString, mt4__pb2.QuoteReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenedOrders(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/OpenedOrders', mt4__pb2.OpenedOrdersRequest.SerializeToString, mt4__pb2.OpenedOrdersReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Symbols(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/Symbols', mt4__pb2.SymbolsRequest.SerializeToString, mt4__pb2.SymbolsReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SymbolParams(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/SymbolParams', mt4__pb2.SymbolParamsRequest.SerializeToString, mt4__pb2.SymbolParamsReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServerTimezone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/ServerTimezone', mt4__pb2.ServerTimezoneRequest.SerializeToString, mt4__pb2.ServerTimezoneReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SymbolParamsMany(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/SymbolParamsMany', mt4__pb2.SymbolParamsManyRequest.SerializeToString, mt4__pb2.SymbolParamsManyReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenedOrder(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/OpenedOrder', mt4__pb2.OpenedOrderRequest.SerializeToString, mt4__pb2.OpenedOrderReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/OrderHistory', mt4__pb2.OrderHistoryRequest.SerializeToString, mt4__pb2.OrderHistoryReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QuoteHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/QuoteHistory', mt4__pb2.QuoteHistoryRequest.SerializeToString, mt4__pb2.QuoteHistoryReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QuoteHistoryMany(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/QuoteHistoryMany', mt4__pb2.QuoteHistoryManyRequest.SerializeToString, mt4__pb2.QuoteHistoryManyReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClosedOrders(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/ClosedOrders', mt4__pb2.ClosedOrdersRequest.SerializeToString, mt4__pb2.ClosedOrdersReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestQuoteHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/RequestQuoteHistory', mt4__pb2.RequestQuoteHistoryRequest.SerializeToString, mt4__pb2.RequestQuoteHistoryReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPlacedType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/SetPlacedType', mt4__pb2.SetPlacedTypeRequest.SerializeToString, mt4__pb2.SetPlacedTypeReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsInvestor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.MT4/IsInvestor', mt4__pb2.IsInvestorRequest.SerializeToString, mt4__pb2.IsInvestorReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class ServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary('/mt4grpc.Service/Ping', request_serializer=mt4__pb2.PingRequest.SerializeToString, response_deserializer=mt4__pb2.PingReply.FromString)
        self.GetLogs = channel.unary_unary('/mt4grpc.Service/GetLogs', request_serializer=mt4__pb2.GetLogsRequest.SerializeToString, response_deserializer=mt4__pb2.GetLogsReply.FromString)
        self.GetLogsByUser = channel.unary_unary('/mt4grpc.Service/GetLogsByUser', request_serializer=mt4__pb2.GetLogsByUserRequest.SerializeToString, response_deserializer=mt4__pb2.GetLogsByUserReply.FromString)
        self.MemorySnapshot = channel.unary_unary('/mt4grpc.Service/MemorySnapshot', request_serializer=mt4__pb2.MemorySnapshotRequest.SerializeToString, response_deserializer=mt4__pb2.MemorySnapshotReply.FromString)
        self.Search = channel.unary_unary('/mt4grpc.Service/Search', request_serializer=mt4__pb2.SearchRequest.SerializeToString, response_deserializer=mt4__pb2.SearchReply.FromString)
        self.GetClients = channel.unary_unary('/mt4grpc.Service/GetClients', request_serializer=mt4__pb2.GetClientsRequest.SerializeToString, response_deserializer=mt4__pb2.GetClientsReply.FromString)
        self.MemoryUsage = channel.unary_unary('/mt4grpc.Service/MemoryUsage', request_serializer=mt4__pb2.MemoryUsageRequest.SerializeToString, response_deserializer=mt4__pb2.MemoryUsageReply.FromString)

class ServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Simple test without parameters
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLogs(self, request, context):
        """Logs for specified token
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLogsByUser(self, request, context):
        """Logs for specified token
        <br> [Example] <br>
        { <br>
        "user": "500476959", <br>
        "password": "ehj4bod" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MemorySnapshot(self, request, context):
        """Memory snapshot
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Broker search by company name
        <br> [Example] <br>
        { <br>
        "company": "" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClients(self, request, context):
        """Return all active with connection state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MemoryUsage(self, request, context):
        """Memory usage details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Ping': grpc.unary_unary_rpc_method_handler(servicer.Ping, request_deserializer=mt4__pb2.PingRequest.FromString, response_serializer=mt4__pb2.PingReply.SerializeToString), 'GetLogs': grpc.unary_unary_rpc_method_handler(servicer.GetLogs, request_deserializer=mt4__pb2.GetLogsRequest.FromString, response_serializer=mt4__pb2.GetLogsReply.SerializeToString), 'GetLogsByUser': grpc.unary_unary_rpc_method_handler(servicer.GetLogsByUser, request_deserializer=mt4__pb2.GetLogsByUserRequest.FromString, response_serializer=mt4__pb2.GetLogsByUserReply.SerializeToString), 'MemorySnapshot': grpc.unary_unary_rpc_method_handler(servicer.MemorySnapshot, request_deserializer=mt4__pb2.MemorySnapshotRequest.FromString, response_serializer=mt4__pb2.MemorySnapshotReply.SerializeToString), 'Search': grpc.unary_unary_rpc_method_handler(servicer.Search, request_deserializer=mt4__pb2.SearchRequest.FromString, response_serializer=mt4__pb2.SearchReply.SerializeToString), 'GetClients': grpc.unary_unary_rpc_method_handler(servicer.GetClients, request_deserializer=mt4__pb2.GetClientsRequest.FromString, response_serializer=mt4__pb2.GetClientsReply.SerializeToString), 'MemoryUsage': grpc.unary_unary_rpc_method_handler(servicer.MemoryUsage, request_deserializer=mt4__pb2.MemoryUsageRequest.FromString, response_serializer=mt4__pb2.MemoryUsageReply.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('mt4grpc.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Service/Ping', mt4__pb2.PingRequest.SerializeToString, mt4__pb2.PingReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLogs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Service/GetLogs', mt4__pb2.GetLogsRequest.SerializeToString, mt4__pb2.GetLogsReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLogsByUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Service/GetLogsByUser', mt4__pb2.GetLogsByUserRequest.SerializeToString, mt4__pb2.GetLogsByUserReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MemorySnapshot(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Service/MemorySnapshot', mt4__pb2.MemorySnapshotRequest.SerializeToString, mt4__pb2.MemorySnapshotReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Service/Search', mt4__pb2.SearchRequest.SerializeToString, mt4__pb2.SearchReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Service/GetClients', mt4__pb2.GetClientsRequest.SerializeToString, mt4__pb2.GetClientsReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MemoryUsage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Service/MemoryUsage', mt4__pb2.MemoryUsageRequest.SerializeToString, mt4__pb2.MemoryUsageReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class SubscriptionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_unary('/mt4grpc.Subscriptions/Subscribe', request_serializer=mt4__pb2.SubscribeRequest.SerializeToString, response_deserializer=mt4__pb2.SubscribeReply.FromString)
        self.SubscribeMany = channel.unary_unary('/mt4grpc.Subscriptions/SubscribeMany', request_serializer=mt4__pb2.SubscribeManyRequest.SerializeToString, response_deserializer=mt4__pb2.SubscribeManyReply.FromString)
        self.UnSubscribe = channel.unary_unary('/mt4grpc.Subscriptions/UnSubscribe', request_serializer=mt4__pb2.UnSubscribeRequest.SerializeToString, response_deserializer=mt4__pb2.UnSubscribeReply.FromString)
        self.UnSubscribeMany = channel.unary_unary('/mt4grpc.Subscriptions/UnSubscribeMany', request_serializer=mt4__pb2.UnSubscribeManyRequest.SerializeToString, response_deserializer=mt4__pb2.UnSubscribeManyReply.FromString)
        self.SubscribeOrderProfit = channel.unary_unary('/mt4grpc.Subscriptions/SubscribeOrderProfit', request_serializer=mt4__pb2.SubscribeOrderProfitRequest.SerializeToString, response_deserializer=mt4__pb2.SubscribeOrderProfitReply.FromString)
        self.SubscribeTickValue = channel.unary_unary('/mt4grpc.Subscriptions/SubscribeTickValue', request_serializer=mt4__pb2.SubscribeTickValueRequest.SerializeToString, response_deserializer=mt4__pb2.SubscribeTickValueReply.FromString)
        self.SubscribeOrderUpdate = channel.unary_unary('/mt4grpc.Subscriptions/SubscribeOrderUpdate', request_serializer=mt4__pb2.SubscribeOrderUpdateRequest.SerializeToString, response_deserializer=mt4__pb2.SubscribeOrderUpdateReply.FromString)
        self.SubscribeQuoteHistory = channel.unary_unary('/mt4grpc.Subscriptions/SubscribeQuoteHistory', request_serializer=mt4__pb2.SubscribeQuoteHistoryRequest.SerializeToString, response_deserializer=mt4__pb2.SubscribeQuoteHistoryReply.FromString)

class SubscriptionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Subscribe(self, request, context):
        """Subscribe symbol for real time quotes and get results via /events socket connection
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "symbol": "EURUSD", <br>
        "interval": "0" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeMany(self, request, context):
        """Subscribe symbosl for real time quotes and get results via /events socket connection
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "interval": "0" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribe(self, request, context):
        """Unsubscribe symbol for real time quotes and get results via /events socket connection
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "symbol": "EURUSD" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeMany(self, request, context):
        """UnSubscribe symbosls for real time quotes and get results via /events socket connection
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeOrderProfit(self, request, context):
        """Subscribe for order profit updates and get results via /events socket connection
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeTickValue(self, request, context):
        """Subscribe symbol for tick value updates
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "symbol": "EURUSD", <br>
        "interval": "0" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeOrderUpdate(self, request, context):
        """Subscribe symbol for tick value updates
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeQuoteHistory(self, request, context):
        """Subscribe quote history
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SubscriptionsServicer_to_server(servicer, server):
    rpc_method_handlers = {'Subscribe': grpc.unary_unary_rpc_method_handler(servicer.Subscribe, request_deserializer=mt4__pb2.SubscribeRequest.FromString, response_serializer=mt4__pb2.SubscribeReply.SerializeToString), 'SubscribeMany': grpc.unary_unary_rpc_method_handler(servicer.SubscribeMany, request_deserializer=mt4__pb2.SubscribeManyRequest.FromString, response_serializer=mt4__pb2.SubscribeManyReply.SerializeToString), 'UnSubscribe': grpc.unary_unary_rpc_method_handler(servicer.UnSubscribe, request_deserializer=mt4__pb2.UnSubscribeRequest.FromString, response_serializer=mt4__pb2.UnSubscribeReply.SerializeToString), 'UnSubscribeMany': grpc.unary_unary_rpc_method_handler(servicer.UnSubscribeMany, request_deserializer=mt4__pb2.UnSubscribeManyRequest.FromString, response_serializer=mt4__pb2.UnSubscribeManyReply.SerializeToString), 'SubscribeOrderProfit': grpc.unary_unary_rpc_method_handler(servicer.SubscribeOrderProfit, request_deserializer=mt4__pb2.SubscribeOrderProfitRequest.FromString, response_serializer=mt4__pb2.SubscribeOrderProfitReply.SerializeToString), 'SubscribeTickValue': grpc.unary_unary_rpc_method_handler(servicer.SubscribeTickValue, request_deserializer=mt4__pb2.SubscribeTickValueRequest.FromString, response_serializer=mt4__pb2.SubscribeTickValueReply.SerializeToString), 'SubscribeOrderUpdate': grpc.unary_unary_rpc_method_handler(servicer.SubscribeOrderUpdate, request_deserializer=mt4__pb2.SubscribeOrderUpdateRequest.FromString, response_serializer=mt4__pb2.SubscribeOrderUpdateReply.SerializeToString), 'SubscribeQuoteHistory': grpc.unary_unary_rpc_method_handler(servicer.SubscribeQuoteHistory, request_deserializer=mt4__pb2.SubscribeQuoteHistoryRequest.FromString, response_serializer=mt4__pb2.SubscribeQuoteHistoryReply.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('mt4grpc.Subscriptions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Subscriptions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Subscribe(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Subscriptions/Subscribe', mt4__pb2.SubscribeRequest.SerializeToString, mt4__pb2.SubscribeReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeMany(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Subscriptions/SubscribeMany', mt4__pb2.SubscribeManyRequest.SerializeToString, mt4__pb2.SubscribeManyReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribe(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Subscriptions/UnSubscribe', mt4__pb2.UnSubscribeRequest.SerializeToString, mt4__pb2.UnSubscribeReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeMany(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Subscriptions/UnSubscribeMany', mt4__pb2.UnSubscribeManyRequest.SerializeToString, mt4__pb2.UnSubscribeManyReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeOrderProfit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Subscriptions/SubscribeOrderProfit', mt4__pb2.SubscribeOrderProfitRequest.SerializeToString, mt4__pb2.SubscribeOrderProfitReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeTickValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Subscriptions/SubscribeTickValue', mt4__pb2.SubscribeTickValueRequest.SerializeToString, mt4__pb2.SubscribeTickValueReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeOrderUpdate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Subscriptions/SubscribeOrderUpdate', mt4__pb2.SubscribeOrderUpdateRequest.SerializeToString, mt4__pb2.SubscribeOrderUpdateReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeQuoteHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Subscriptions/SubscribeQuoteHistory', mt4__pb2.SubscribeQuoteHistoryRequest.SerializeToString, mt4__pb2.SubscribeQuoteHistoryReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class TradingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OrderSend = channel.unary_unary('/mt4grpc.Trading/OrderSend', request_serializer=mt4__pb2.OrderSendRequest.SerializeToString, response_deserializer=mt4__pb2.OrderSendReply.FromString)
        self.OrderModify = channel.unary_unary('/mt4grpc.Trading/OrderModify', request_serializer=mt4__pb2.OrderModifyRequest.SerializeToString, response_deserializer=mt4__pb2.OrderModifyReply.FromString)
        self.OrderCloseBy = channel.unary_unary('/mt4grpc.Trading/OrderCloseBy', request_serializer=mt4__pb2.OrderCloseByRequest.SerializeToString, response_deserializer=mt4__pb2.OrderCloseByReply.FromString)
        self.OrderDelete = channel.unary_unary('/mt4grpc.Trading/OrderDelete', request_serializer=mt4__pb2.OrderDeleteRequest.SerializeToString, response_deserializer=mt4__pb2.OrderDeleteReply.FromString)
        self.OrderClose = channel.unary_unary('/mt4grpc.Trading/OrderClose', request_serializer=mt4__pb2.OrderCloseRequest.SerializeToString, response_deserializer=mt4__pb2.OrderCloseReply.FromString)

class TradingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OrderSend(self, request, context):
        """Send market or pending order
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "symbol": "EURUSD", <br>
        "operation": "Buy", <br>
        "volume": "0.1", <br>
        "price": "0", <br>
        "slippage": "0", <br>
        "stoploss": "0", <br>
        "takeprofit": "0", <br>
        "magic": "0", <br>
        "placedType": "Client" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderModify(self, request, context):
        """Modify market or pending order
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "ticket": "0", <br>
        "stoploss": "0", <br>
        "takeprofit": "0", <br>
        "price": "0" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderCloseBy(self, request, context):
        """Close market order with opposite market order
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "ticket1": "0", <br>
        "ticket2": "0" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderDelete(self, request, context):
        """Delete pending order
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "ticket": "0" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderClose(self, request, context):
        """Close market order with opposite market order
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4", <br>
        "ticket": "0", <br>
        "lots": "0", <br>
        "price": "0", <br>
        "slippage": "0" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_TradingServicer_to_server(servicer, server):
    rpc_method_handlers = {'OrderSend': grpc.unary_unary_rpc_method_handler(servicer.OrderSend, request_deserializer=mt4__pb2.OrderSendRequest.FromString, response_serializer=mt4__pb2.OrderSendReply.SerializeToString), 'OrderModify': grpc.unary_unary_rpc_method_handler(servicer.OrderModify, request_deserializer=mt4__pb2.OrderModifyRequest.FromString, response_serializer=mt4__pb2.OrderModifyReply.SerializeToString), 'OrderCloseBy': grpc.unary_unary_rpc_method_handler(servicer.OrderCloseBy, request_deserializer=mt4__pb2.OrderCloseByRequest.FromString, response_serializer=mt4__pb2.OrderCloseByReply.SerializeToString), 'OrderDelete': grpc.unary_unary_rpc_method_handler(servicer.OrderDelete, request_deserializer=mt4__pb2.OrderDeleteRequest.FromString, response_serializer=mt4__pb2.OrderDeleteReply.SerializeToString), 'OrderClose': grpc.unary_unary_rpc_method_handler(servicer.OrderClose, request_deserializer=mt4__pb2.OrderCloseRequest.FromString, response_serializer=mt4__pb2.OrderCloseReply.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('mt4grpc.Trading', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Trading(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OrderSend(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Trading/OrderSend', mt4__pb2.OrderSendRequest.SerializeToString, mt4__pb2.OrderSendReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderModify(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Trading/OrderModify', mt4__pb2.OrderModifyRequest.SerializeToString, mt4__pb2.OrderModifyReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderCloseBy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Trading/OrderCloseBy', mt4__pb2.OrderCloseByRequest.SerializeToString, mt4__pb2.OrderCloseByReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderDelete(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Trading/OrderDelete', mt4__pb2.OrderDeleteRequest.SerializeToString, mt4__pb2.OrderDeleteReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderClose(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mt4grpc.Trading/OrderClose', mt4__pb2.OrderCloseRequest.SerializeToString, mt4__pb2.OrderCloseReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class StreamsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnOrderUpdate = channel.unary_stream('/mt4grpc.Streams/OnOrderUpdate', request_serializer=mt4__pb2.OnOrderUpdateRequest.SerializeToString, response_deserializer=mt4__pb2.OnOrderUpdateReply.FromString)
        self.OnQuote = channel.unary_stream('/mt4grpc.Streams/OnQuote', request_serializer=mt4__pb2.OnQuoteRequest.SerializeToString, response_deserializer=mt4__pb2.OnQuoteReply.FromString)
        self.OnTickValue = channel.unary_stream('/mt4grpc.Streams/OnTickValue', request_serializer=mt4__pb2.OnTickValueRequest.SerializeToString, response_deserializer=mt4__pb2.OnTickValueReply.FromString)
        self.OnOrderProfit = channel.unary_stream('/mt4grpc.Streams/OnOrderProfit', request_serializer=mt4__pb2.OnOrderProfitRequest.SerializeToString, response_deserializer=mt4__pb2.OnOrderProfitReply.FromString)

class StreamsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OnOrderUpdate(self, request, context):
        """All trading activity on accont.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnQuote(self, request, context):
        """Real time quotes.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnTickValue(self, request, context):
        """Real time quotes.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnOrderProfit(self, request, context):
        """Orders profits updates.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        Quote history .
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        rpc OnQuoteHistory (OnQuoteHistoryRequest) returns (OnQuoteHistoryReply);
        On disconnect event.
        <br> [Example] <br>
        { <br>
        "id": "demo-token-mt4" <br>
        }
        rpc OnDisconnect (OnDisconnectRequest) returns (OnDisconnectReply);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_StreamsServicer_to_server(servicer, server):
    rpc_method_handlers = {'OnOrderUpdate': grpc.unary_stream_rpc_method_handler(servicer.OnOrderUpdate, request_deserializer=mt4__pb2.OnOrderUpdateRequest.FromString, response_serializer=mt4__pb2.OnOrderUpdateReply.SerializeToString), 'OnQuote': grpc.unary_stream_rpc_method_handler(servicer.OnQuote, request_deserializer=mt4__pb2.OnQuoteRequest.FromString, response_serializer=mt4__pb2.OnQuoteReply.SerializeToString), 'OnTickValue': grpc.unary_stream_rpc_method_handler(servicer.OnTickValue, request_deserializer=mt4__pb2.OnTickValueRequest.FromString, response_serializer=mt4__pb2.OnTickValueReply.SerializeToString), 'OnOrderProfit': grpc.unary_stream_rpc_method_handler(servicer.OnOrderProfit, request_deserializer=mt4__pb2.OnOrderProfitRequest.FromString, response_serializer=mt4__pb2.OnOrderProfitReply.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('mt4grpc.Streams', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Streams(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OnOrderUpdate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mt4grpc.Streams/OnOrderUpdate', mt4__pb2.OnOrderUpdateRequest.SerializeToString, mt4__pb2.OnOrderUpdateReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnQuote(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mt4grpc.Streams/OnQuote', mt4__pb2.OnQuoteRequest.SerializeToString, mt4__pb2.OnQuoteReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnTickValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mt4grpc.Streams/OnTickValue', mt4__pb2.OnTickValueRequest.SerializeToString, mt4__pb2.OnTickValueReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnOrderProfit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mt4grpc.Streams/OnOrderProfit', mt4__pb2.OnOrderProfitRequest.SerializeToString, mt4__pb2.OnOrderProfitReply.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)