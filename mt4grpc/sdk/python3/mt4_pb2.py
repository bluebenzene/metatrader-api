"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tmt4.proto\x12\x07mt4grpc\x1a\x1fgoogle/protobuf/timestamp.proto"N\n\x05Error\x12 \n\x04code\x18\x01 \x01(\x0e2\x12.mt4grpc.ErrorCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nstackTrace\x18\x03 \x01(\t"L\n\x0eConnectRequest\x12\x0c\n\x04user\x18\x01 \x01(\x05\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05"=\n\x0cConnectReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"!\n\x13CheckConnectRequest\x12\n\n\x02id\x18\x01 \x01(\t"B\n\x11CheckConnectReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x1f\n\x11DisconnectRequest\x12\n\n\x02id\x18\x01 \x01(\t"@\n\x0fDisconnectReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"#\n\x15AccountSummaryRequest\x12\n\n\x02id\x18\x01 \x01(\t"\xe6\x01\n\x0eAccountSummary\x12\x0f\n\x07Balance\x18\x01 \x01(\x01\x12\x0e\n\x06Credit\x18\x02 \x01(\x01\x12\x0e\n\x06Profit\x18\x03 \x01(\x01\x12\x0e\n\x06Equity\x18\x04 \x01(\x01\x12\x0e\n\x06Margin\x18\x05 \x01(\x01\x12\x12\n\nFreeMargin\x18\x06 \x01(\x01\x12\x13\n\x0bMarginLevel\x18\x07 \x01(\x01\x12\x10\n\x08Leverage\x18\x08 \x01(\x01\x12\x10\n\x08Currency\x18\t \x01(\t\x12"\n\x04Type\x18\n \x01(\x0e2\x14.mt4grpc.AccountType\x12\x12\n\nIsInvestor\x18\x0b \x01(\x08"]\n\x13AccountSummaryReply\x12\'\n\x06result\x18\x01 \x01(\x0b2\x17.mt4grpc.AccountSummary\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x1b\n\rGroupsRequest\x12\n\n\x02id\x18\x01 \x01(\t"3\n\x0eConSymbolGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t"U\n\x0bGroupsReply\x12\'\n\x06result\x18\x01 \x03(\x0b2\x17.mt4grpc.ConSymbolGroup\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"*\n\x0cQuoteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t"\x7f\n\x0eQuoteEventArgs\x12\x0e\n\x06Symbol\x18\x01 \x01(\t\x12\x0b\n\x03Bid\x18\x02 \x01(\x01\x12\x0b\n\x03Ask\x18\x03 \x01(\x01\x12(\n\x04Time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04High\x18\x05 \x01(\x01\x12\x0b\n\x03Low\x18\x06 \x01(\x01"T\n\nQuoteReply\x12\'\n\x06result\x18\x01 \x01(\x0b2\x17.mt4grpc.QuoteEventArgs\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"!\n\x13OpenedOrdersRequest\x12\n\n\x02id\x18\x01 \x01(\t"\xe4\x03\n\x05Order\x12\'\n\nPlacedType\x18\x01 \x01(\x0e2\x13.mt4grpc.PlacedType\x12\x0e\n\x06Ticket\x18\x02 \x01(\x05\x12,\n\x08OpenTime\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12-\n\tCloseTime\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nExpiration\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x19\n\x04Type\x18\x06 \x01(\x0e2\x0b.mt4grpc.Op\x12\x0c\n\x04Lots\x18\x07 \x01(\x01\x12\x0e\n\x06Symbol\x18\x08 \x01(\t\x12\x11\n\tOpenPrice\x18\t \x01(\x01\x12\x10\n\x08StopLoss\x18\n \x01(\x01\x12\x12\n\nTakeProfit\x18\x0b \x01(\x01\x12\x12\n\nClosePrice\x18\x0c \x01(\x01\x12\x13\n\x0bMagicNumber\x18\r \x01(\x05\x12\x0c\n\x04Swap\x18\x0e \x01(\x01\x12\x12\n\nCommission\x18\x0f \x01(\x01\x12\x0f\n\x07Comment\x18\x10 \x01(\t\x12\x0e\n\x06Profit\x18\x11 \x01(\x01\x12\x10\n\x08RateOpen\x18\x12 \x01(\x01\x12\x11\n\tRateClose\x18\x13 \x01(\x01\x12\x12\n\nRateMargin\x18\x14 \x01(\x01"R\n\x11OpenedOrdersReply\x12\x1e\n\x06result\x18\x01 \x03(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x1c\n\x0eSymbolsRequest\x12\n\n\x02id\x18\x01 \x01(\t"=\n\x0cSymbolsReply\x12\x0e\n\x06result\x18\x01 \x03(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"1\n\x13SymbolParamsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t"\x9a\x01\n\x0cSymbolParams\x12\x12\n\nSymbolName\x18\x01 \x01(\t\x12#\n\x06Symbol\x18\x02 \x01(\x0b2\x13.mt4grpc.SymbolInfo\x12&\n\x05Group\x18\x03 \x01(\x0b2\x17.mt4grpc.ConSymbolGroup\x12)\n\x0bGroupParams\x18\x04 \x01(\x0b2\x14.mt4grpc.ConGroupSec"\xe7\x02\n\nSymbolInfo\x12%\n\tExecution\x18\x01 \x01(\x0e2\x12.mt4grpc.Execution\x12\x12\n\nStopsLevel\x18\x02 \x01(\x05\x12\x0e\n\x06Digits\x18\x03 \x01(\x05\x12\r\n\x05Point\x18\x04 \x01(\x01\x12\x10\n\x08SwapLong\x18\x05 \x01(\x01\x12\x11\n\tSwapShort\x18\x06 \x01(\x01\x12\x0e\n\x06Spread\x18\x07 \x01(\x05\x12\x13\n\x0bFreezeLevel\x18\x08 \x01(\x05\x12\x16\n\x0eMarginCurrency\x18\t \x01(\t\x12\'\n\nProfitMode\x18\n \x01(\x0e2\x13.mt4grpc.ProfitMode\x12\'\n\nMarginMode\x18\x0b \x01(\x0e2\x13.mt4grpc.MarginMode\x12\x14\n\x0cContractSize\x18\x0c \x01(\x01\x12\x10\n\x08Currency\x18\r \x01(\t\x12\x15\n\rMarginDivider\x18\x0e \x01(\x01\x12\x0c\n\x04Code\x18\x0f \x01(\x05"\xd5\x03\n\x0bConGroupSec\x12\x0e\n\x06MinLot\x18\x01 \x01(\x01\x12\x0e\n\x06MaxLot\x18\x02 \x01(\x01\x12\x0f\n\x07LotStep\x18\x03 \x01(\x01\x12\x0c\n\x04show\x18\x04 \x01(\x05\x12\r\n\x05trade\x18\x05 \x01(\x05\x12\x11\n\texecution\x18\x06 \x01(\x05\x12\x11\n\tcomm_base\x18\x07 \x01(\x01\x12\x11\n\tcomm_type\x18\x08 \x01(\x05\x12\x11\n\tcomm_lots\x18\t \x01(\x05\x12\x12\n\ncomm_agent\x18\n \x01(\x01\x12\x17\n\x0fcomm_agent_type\x18\x0b \x01(\x05\x12\x13\n\x0bspread_diff\x18\x0c \x01(\x05\x12\x0f\n\x07lot_min\x18\r \x01(\x05\x12\x0f\n\x07lot_max\x18\x0e \x01(\x05\x12\x14\n\x0cie_deviation\x18\x0f \x01(\x05\x12\x14\n\x0cconfirmation\x18\x10 \x01(\x05\x12\x14\n\x0ctrade_rights\x18\x11 \x01(\x05\x12\x15\n\rie_quick_mode\x18\x12 \x01(\x05\x12\x19\n\x11autocloseout_mode\x18\x13 \x01(\x05\x12\x10\n\x08comm_tax\x18\x14 \x01(\x01\x12\x17\n\x0fcomm_agent_lots\x18\x15 \x01(\x05\x12\x17\n\x0ffreemargin_mode\x18\x16 \x01(\x05\x12\x10\n\x08reserved\x18\x17 \x03(\x05"Y\n\x11SymbolParamsReply\x12%\n\x06result\x18\x01 \x01(\x0b2\x15.mt4grpc.SymbolParams\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"#\n\x15ServerTimezoneRequest\x12\n\n\x02id\x18\x01 \x01(\t"D\n\x13ServerTimezoneReply\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x1f\n\x11IsInvestorRequest\x12\n\n\x02id\x18\x01 \x01(\t"@\n\x0fIsInvestorReply\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"6\n\x17SymbolParamsManyRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07symbols\x18\x02 \x03(\t"]\n\x15SymbolParamsManyReply\x12%\n\x06result\x18\x01 \x03(\x0b2\x15.mt4grpc.SymbolParams\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"0\n\x12OpenedOrderRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06ticket\x18\x02 \x01(\x05"Q\n\x10OpenedOrderReply\x12\x1e\n\x06result\x18\x01 \x01(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error";\n\x13OrderHistoryRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04from\x18\x02 \x01(\t\x12\n\n\x02to\x18\x03 \x01(\t"R\n\x11OrderHistoryReply\x12\x1e\n\x06result\x18\x01 \x03(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"u\n\x13QuoteHistoryRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12%\n\ttimeframe\x18\x03 \x01(\x0e2\x12.mt4grpc.Timeframe\x12\x0c\n\x04from\x18\x04 \x01(\t\x12\r\n\x05count\x18\x05 \x01(\x05"w\n\x03Bar\x12(\n\x04Time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04Open\x18\x02 \x01(\x01\x12\x0c\n\x04High\x18\x03 \x01(\x01\x12\x0b\n\x03Low\x18\x04 \x01(\x01\x12\r\n\x05Close\x18\x05 \x01(\x01\x12\x0e\n\x06Volume\x18\x06 \x01(\x01"P\n\x11QuoteHistoryReply\x12\x1c\n\x06result\x18\x01 \x03(\x0b2\x0c.mt4grpc.Bar\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"y\n\x17QuoteHistoryManyRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x03(\t\x12%\n\ttimeframe\x18\x03 \x01(\x0e2\x12.mt4grpc.Timeframe\x12\x0c\n\x04from\x18\x04 \x01(\t\x12\r\n\x05count\x18\x05 \x01(\x05"N\n\rBarsForSymbol\x12\x0e\n\x06Symbol\x18\x01 \x01(\t\x12\x1a\n\x04Bars\x18\x02 \x03(\x0b2\x0c.mt4grpc.Bar\x12\x11\n\tException\x18\x03 \x01(\t"^\n\x15QuoteHistoryManyReply\x12&\n\x06result\x18\x01 \x03(\x0b2\x16.mt4grpc.BarsForSymbol\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"!\n\x13ClosedOrdersRequest\x12\n\n\x02id\x18\x01 \x01(\t"R\n\x11ClosedOrdersReply\x12\x1e\n\x06result\x18\x01 \x03(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"|\n\x1aRequestQuoteHistoryRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12%\n\ttimeframe\x18\x03 \x01(\x0e2\x12.mt4grpc.Timeframe\x12\x0c\n\x04from\x18\x04 \x01(\t\x12\r\n\x05count\x18\x05 \x01(\x05"I\n\x18RequestQuoteHistoryReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"E\n\x14SetPlacedTypeRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x04type\x18\x02 \x01(\x0e2\x13.mt4grpc.PlacedType"S\n\x12SetPlacedTypeReply\x12\x1e\n\x06result\x18\x01 \x03(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\r\n\x0bPingRequest":\n\tPingReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x1c\n\x0eGetLogsRequest\x12\n\n\x02id\x18\x01 \x01(\t"\x96\x01\n\x06LogRec\x12(\n\x04Time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12%\n\x05Level\x18\x02 \x01(\x0e2\x16.mt4grpc.LogEventLevel\x12\x0f\n\x07Message\x18\x03 \x01(\t\x12\n\n\x02Id\x18\x04 \x01(\t\x12\x0c\n\x04User\x18\x05 \x01(\x05\x12\x10\n\x08Password\x18\x06 \x01(\t"N\n\x0cGetLogsReply\x12\x1f\n\x06result\x18\x01 \x03(\x0b2\x0f.mt4grpc.LogRec\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"6\n\x14GetLogsByUserRequest\x12\x0c\n\x04user\x18\x01 \x01(\x05\x12\x10\n\x08password\x18\x02 \x01(\t"T\n\x12GetLogsByUserReply\x12\x1f\n\x06result\x18\x01 \x03(\x0b2\x0f.mt4grpc.LogRec\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x17\n\x15MemorySnapshotRequest"D\n\x13MemorySnapshotReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error" \n\rSearchRequest\x12\x0f\n\x07company\x18\x01 \x01(\t"<\n\x12BrokerSerachResult\x12&\n\x06Result\x18\x01 \x03(\x0b2\x16.mt4grpc.BrokerCompany"H\n\rBrokerCompany\x12\x0f\n\x07Company\x18\x01 \x01(\t\x12&\n\x07Results\x18\x02 \x03(\x0b2\x15.mt4grpc.BrokerServer"=\n\x0cBrokerServer\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0e\n\x06Access\x18\x02 \x03(\t\x12\x0f\n\x07Is_demo\x18\x03 \x01(\t"Y\n\x0bSearchReply\x12+\n\x06result\x18\x01 \x01(\x0b2\x1b.mt4grpc.BrokerSerachResult\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x13\n\x11GetClientsRequest"W\n\x0cClientStatus\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x11\n\tConnected\x18\x02 \x01(\x08\x12\x0c\n\x04User\x18\x03 \x01(\x05\x12\x0c\n\x04Host\x18\x04 \x01(\t\x12\x0c\n\x04Port\x18\x05 \x01(\x05"W\n\x0fGetClientsReply\x12%\n\x06result\x18\x01 \x03(\x0b2\x15.mt4grpc.ClientStatus\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x14\n\x12MemoryUsageRequest"\xe8\x03\n\x08MemUsage\x12\x16\n\x0eIs64BitProcess\x18\x01 \x01(\x08\x12\x1b\n\x13PhysicalMemoryUsage\x18\x02 \x01(\x05\x12\x14\n\x0cBasePriority\x18\x03 \x01(\x05\x12\x15\n\rPriorityClass\x18\x04 \x01(\t\x12\x19\n\x11UserProcessorTime\x18\x05 \x01(\t\x12\x1f\n\x17PrivilegedProcessorTime\x18\x06 \x01(\t\x12\x1a\n\x12TotalProcessorTime\x18\x07 \x01(\t\x12\x1d\n\x15PagedSystemMemorySize\x18\x08 \x01(\x05\x12\x17\n\x0fPagedMemorySize\x18\t \x01(\x05\x12\x14\n\x0cPeakPagedMem\x18\n \x01(\x05\x12\x16\n\x0ePeakVirtualMem\x18\x0b \x01(\x05\x12\x16\n\x0ePeakWorkingSet\x18\x0c \x01(\x05\x12\x17\n\x0fMemoryLoadBytes\x18\r \x01(\x05\x12\x15\n\rHeapSizeBytes\x18\x0e \x01(\x05\x12\x17\n\x0fFragmentedBytes\x18\x0f \x01(\x05\x12$\n\x1cHighMemoryLoadThresholdBytes\x18\x10 \x01(\x05\x12!\n\x19TotalAvailableMemoryBytes\x18\x11 \x01(\x05\x12\x12\n\nResponding\x18\x12 \x01(\x08"T\n\x10MemoryUsageReply\x12!\n\x06result\x18\x01 \x01(\x0b2\x11.mt4grpc.MemUsage\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"@\n\x10SubscribeRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\x05"?\n\x0eSubscribeReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"E\n\x14SubscribeManyRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07symbols\x18\x02 \x03(\t\x12\x10\n\x08interval\x18\x03 \x01(\x05"C\n\x12SubscribeManyReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"0\n\x12UnSubscribeRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t"A\n\x10UnSubscribeReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"5\n\x16UnSubscribeManyRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07symbols\x18\x02 \x03(\t"E\n\x14UnSubscribeManyReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error")\n\x1bSubscribeOrderProfitRequest\x12\n\n\x02id\x18\x01 \x01(\t"Z\n\x19SubscribeOrderProfitReply\x12\x1e\n\x06result\x18\x01 \x03(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"I\n\x19SubscribeTickValueRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\x05"H\n\x17SubscribeTickValueReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error")\n\x1bSubscribeOrderUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t"Z\n\x19SubscribeOrderUpdateReply\x12\x1e\n\x06result\x18\x01 \x03(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"*\n\x1cSubscribeQuoteHistoryRequest\x12\n\n\x02id\x18\x01 \x01(\t"K\n\x1aSubscribeQuoteHistoryReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x82\x02\n\x10OrderSendRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x1e\n\toperation\x18\x03 \x01(\x0e2\x0b.mt4grpc.Op\x12\x0e\n\x06volume\x18\x04 \x01(\x01\x12\r\n\x05price\x18\x05 \x01(\x01\x12\x10\n\x08slippage\x18\x06 \x01(\x05\x12\x10\n\x08stoploss\x18\x07 \x01(\x01\x12\x12\n\ntakeprofit\x18\x08 \x01(\x01\x12\x0f\n\x07comment\x18\t \x01(\t\x12\r\n\x05magic\x18\n \x01(\x05\x12\x12\n\nexpiration\x18\x0b \x01(\t\x12\'\n\nplacedType\x18\x0c \x01(\x0e2\x13.mt4grpc.PlacedType"O\n\x0eOrderSendReply\x12\x1e\n\x06result\x18\x01 \x01(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"y\n\x12OrderModifyRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06ticket\x18\x02 \x01(\x05\x12\x10\n\x08stoploss\x18\x03 \x01(\x01\x12\x12\n\ntakeprofit\x18\x04 \x01(\x01\x12\r\n\x05price\x18\x05 \x01(\x01\x12\x12\n\nexpiration\x18\x06 \x01(\t"Q\n\x10OrderModifyReply\x12\x1e\n\x06result\x18\x01 \x01(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"C\n\x13OrderCloseByRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07ticket1\x18\x02 \x01(\x05\x12\x0f\n\x07ticket2\x18\x03 \x01(\x05"B\n\x11OrderCloseByReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"0\n\x12OrderDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06ticket\x18\x02 \x01(\x05"A\n\x10OrderDeleteReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"^\n\x11OrderCloseRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06ticket\x18\x02 \x01(\x05\x12\x0c\n\x04lots\x18\x03 \x01(\x01\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x10\n\x08slippage\x18\x05 \x01(\x05"P\n\x0fOrderCloseReply\x12\x1e\n\x06result\x18\x01 \x01(\x0b2\x0e.mt4grpc.Order\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x1b\n\rEventsRequest\x12\n\n\x02id\x18\x01 \x01(\t"<\n\x0bEventsReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error""\n\x14OnOrderUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t"\xbe\x01\n\x12OrderUpdateSummary\x12-\n\x06Update\x18\x01 \x01(\x0b2\x1d.mt4grpc.OrderUpdateEventArgs\x12\x0f\n\x07Balance\x18\x02 \x01(\x01\x12\x0e\n\x06Equity\x18\x03 \x01(\x01\x12\x0e\n\x06Margin\x18\x04 \x01(\x01\x12\x12\n\nFreeMargin\x18\x05 \x01(\x01\x12\x0e\n\x06Profit\x18\x06 \x01(\x01\x12$\n\x0cOpenedOrders\x18\x07 \x03(\x0b2\x0e.mt4grpc.Order"\\\n\x14OrderUpdateEventArgs\x12\x1d\n\x05Order\x18\x01 \x01(\x0b2\x0e.mt4grpc.Order\x12%\n\x06Action\x18\x02 \x01(\x0e2\x15.mt4grpc.UpdateAction"`\n\x12OnOrderUpdateReply\x12+\n\x06result\x18\x01 \x01(\x0b2\x1b.mt4grpc.OrderUpdateSummary\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"\x1c\n\x0eOnQuoteRequest\x12\n\n\x02id\x18\x01 \x01(\t"V\n\x0cOnQuoteReply\x12\'\n\x06result\x18\x01 \x01(\x0b2\x17.mt4grpc.QuoteEventArgs\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error" \n\x12OnTickValueRequest\x12\n\n\x02id\x18\x01 \x01(\t"4\n\x0fSymbolTickValue\x12\x0e\n\x06Symbol\x18\x01 \x01(\t\x12\x11\n\tTickValue\x18\x02 \x01(\x01"[\n\x10OnTickValueReply\x12(\n\x06result\x18\x01 \x01(\x0b2\x18.mt4grpc.SymbolTickValue\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error""\n\x14OnOrderProfitRequest\x12\n\n\x02id\x18\x01 \x01(\t"\x83\x01\n\x0cProfitUpdate\x12\x0f\n\x07Balance\x18\x01 \x01(\x01\x12\x0e\n\x06Equity\x18\x02 \x01(\x01\x12\x0e\n\x06Margin\x18\x03 \x01(\x01\x12\x12\n\nFreeMargin\x18\x04 \x01(\x01\x12\x0e\n\x06Profit\x18\x05 \x01(\x01\x12\x1e\n\x06Orders\x18\x06 \x03(\x0b2\x0e.mt4grpc.Order"Z\n\x12OnOrderProfitReply\x12%\n\x06result\x18\x01 \x01(\x0b2\x15.mt4grpc.ProfitUpdate\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"#\n\x15OnQuoteHistoryRequest\x12\n\n\x02id\x18\x01 \x01(\t"j\n\x15QuoteHistoryEventArgs\x12\x0e\n\x06Symbol\x18\x01 \x01(\t\x12%\n\tTimeframe\x18\x02 \x01(\x0e2\x12.mt4grpc.Timeframe\x12\x1a\n\x04Bars\x18\x03 \x03(\x0b2\x0c.mt4grpc.Bar"d\n\x13OnQuoteHistoryReply\x12.\n\x06result\x18\x01 \x01(\x0b2\x1e.mt4grpc.QuoteHistoryEventArgs\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error"!\n\x13OnDisconnectRequest\x12\n\n\x02id\x18\x01 \x01(\t"B\n\x11OnDisconnectReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x1d\n\x05error\x18\x02 \x01(\x0b2\x0e.mt4grpc.Error*R\n\x0bAccountType\x12\x14\n\x10AccountType_Real\x10\x00\x12\x17\n\x13AccountType_Contest\x10\x01\x12\x14\n\x10AccountType_Demo\x10\x02*\xd7\x01\n\nPlacedType\x12\x15\n\x11PlacedType_Client\x10\x00\x12\x15\n\x11PlacedType_Expert\x10\x01\x12\x15\n\x11PlacedType_Dealer\x10\x02\x12\x15\n\x11PlacedType_Signal\x10\x03\x12\x16\n\x12PlacedType_Gateway\x10\x04\x12\x15\n\x11PlacedType_Mobile\x10\x05\x12\x12\n\x0ePlacedType_Web\x10\x06\x12\x12\n\x0ePlacedType_Api\x10\x07\x12\x16\n\x12PlacedType_Default\x10\x08*\x80\x01\n\x02Op\x12\n\n\x06Op_Buy\x10\x00\x12\x0b\n\x07Op_Sell\x10\x01\x12\x0f\n\x0bOp_BuyLimit\x10\x02\x12\x10\n\x0cOp_SellLimit\x10\x03\x12\x0e\n\nOp_BuyStop\x10\x04\x12\x0f\n\x0bOp_SellStop\x10\x05\x12\x0e\n\nOp_Balance\x10\x06\x12\r\n\tOp_Credit\x10\x07*O\n\tExecution\x12\x15\n\x11Execution_Request\x10\x00\x12\x15\n\x11Execution_Instant\x10\x01\x12\x14\n\x10Execution_Market\x10\x02*N\n\nProfitMode\x12\x14\n\x10ProfitMode_Forex\x10\x00\x12\x12\n\x0eProfitMode_CFD\x10\x01\x12\x16\n\x12ProfitMode_Futures\x10\x02*\x83\x01\n\nMarginMode\x12\x14\n\x10MarginMode_Forex\x10\x00\x12\x12\n\x0eMarginMode_CFD\x10\x01\x12\x16\n\x12MarginMode_Futures\x10\x02\x12\x17\n\x13MarginMode_CfdIndex\x10\x03\x12\x1a\n\x16MarginMode_CfdLeverage\x10\x04*\xc7\x01\n\tTimeframe\x12\x10\n\x0cTIMEFRAME_M0\x10\x00\x12\x10\n\x0cTimeframe_M1\x10\x01\x12\x10\n\x0cTimeframe_M5\x10\x05\x12\x11\n\rTimeframe_M15\x10\x0f\x12\x11\n\rTimeframe_M30\x10\x1e\x12\x10\n\x0cTimeframe_H1\x10<\x12\x11\n\x0cTimeframe_H4\x10\xf0\x01\x12\x11\n\x0cTimeframe_D1\x10\xa0\x0b\x12\x11\n\x0cTimeframe_W1\x10\xe0N\x12\x13\n\rTimeframe_MN1\x10\xc0\xd1\x02*\xaf\x01\n\rLogEventLevel\x12\x19\n\x15LogEventLevel_Verbose\x10\x00\x12\x17\n\x13LogEventLevel_Debug\x10\x01\x12\x1d\n\x19LogEventLevel_Information\x10\x02\x12\x19\n\x15LogEventLevel_Warning\x10\x03\x12\x17\n\x13LogEventLevel_Error\x10\x04\x12\x17\n\x13LogEventLevel_Fatal\x10\x05*\x9c\x02\n\x0cUpdateAction\x12\x1d\n\x19UpdateAction_PositionOpen\x10\x00\x12\x1e\n\x1aUpdateAction_PositionClose\x10\x01\x12\x1f\n\x1bUpdateAction_PositionModify\x10\x02\x12\x1c\n\x18UpdateAction_PendingOpen\x10\x03\x12\x1d\n\x19UpdateAction_PendingClose\x10\x04\x12\x1e\n\x1aUpdateAction_PendingModify\x10\x05\x12\x1c\n\x18UpdateAction_PendingFill\x10\x06\x12\x18\n\x14UpdateAction_Balance\x10\x07\x12\x17\n\x13UpdateAction_Credit\x10\x08*\xc6\x07\n\tErrorCode\x12\x12\n\x0eINTERNAL_ERROR\x10\x00\x12\x10\n\x0cCOMMON_ERROR\x10\x02\x12\x11\n\rINVALID_PARAM\x10\x03\x12\x0f\n\x0bSERVER_BUSY\x10\x04\x12\x0f\n\x0bOLD_VERSION\x10\x05\x12\x0e\n\nNO_CONNECT\x10\x06\x12\x15\n\x11NOT_ENOUGH_RIGHTS\x10\x07\x12\x18\n\x14TOO_FREQUENT_REQUEST\x10\x08\x12\x11\n\rNO_CONNECTION\x10\n\x12\x19\n\x15SERVICE_NOT_AVAILABLE\x10\x0b\x12\x19\n\x15TOO_FREQUENT_REQUESTS\x10\x0c\x12\x17\n\x13SECRET_KEY_REQUIRED\x10\r\x12\x1c\n\x18INVALID_ONETIME_PASSWORD\x10\x0e\x12\x14\n\x10ACCOUNT_DISABLED\x10@\x12\x13\n\x0fINVALID_ACCOUNT\x10A\x12\x18\n\x14PUBLIC_KEY_NOT_FOUND\x10B\x12\x12\n\rTRADE_TIMEOUT\x10\x80\x01\x12\x13\n\x0eINVALID_PRICES\x10\x81\x01\x12\x12\n\rINVALID_SL_TP\x10\x82\x01\x12\x13\n\x0eINVALID_VOLUME\x10\x83\x01\x12\x12\n\rMARKET_CLOSED\x10\x84\x01\x12\x13\n\x0eTRADE_DISABLED\x10\x85\x01\x12\x0e\n\tNOT_MONEY\x10\x86\x01\x12\x12\n\rPRICE_CHANGED\x10\x87\x01\x12\x0f\n\nOFF_QUOTES\x10\x88\x01\x12\x10\n\x0bBROKER_BUSY\x10\x89\x01\x12\x0c\n\x07REQUOTE\x10\x8a\x01\x12\x11\n\x0cORDER_LOCKED\x10\x8b\x01\x12\x15\n\x10LONG_POS_ALLOWED\x10\x8c\x01\x12\x16\n\x11TOO_MANY_REQUESTS\x10\x8d\x01\x12\x13\n\x0eORDER_ACCEPTED\x10\x8e\x01\x12\x15\n\x10ORDER_IN_PROCESS\x10\x8f\x01\x12\x16\n\x11REQUEST_CANCELLED\x10\x90\x01\x12\x19\n\x14MODIFICATIONS_DENIED\x10\x91\x01\x12\x17\n\x12TRADE_CONTEXT_BUSY\x10\x92\x01\x12\x18\n\x13EXPIRATION_DISABLED\x10\x93\x01\x12\x14\n\x0fTOO_MANY_ORDERS\x10\x94\x01\x12\x15\n\x10HEDGE_PROHIBITED\x10\x95\x01\x12\x15\n\x10RPROHIBITED_FIFO\x10\x96\x01\x12\x12\n\rINVALID_TOKEN\x10\x80\x02\x12\x13\n\x0eINVALID_SYMBOL\x10\x81\x02\x12\x13\n\x0eINVALID_TICKET\x10\x82\x02\x12\x10\n\x0bSAME_PARAMS\x10\x83\x02\x12\x12\n\rCONNECT_ERROR\x10\x84\x02\x12\x0c\n\x07TIMEOUT\x10\x85\x022\xd5\x01\n\nConnection\x129\n\x07Connect\x12\x17.mt4grpc.ConnectRequest\x1a\x15.mt4grpc.ConnectReply\x12H\n\x0cCheckConnect\x12\x1c.mt4grpc.CheckConnectRequest\x1a\x1a.mt4grpc.CheckConnectReply\x12B\n\nDisconnect\x12\x1a.mt4grpc.DisconnectRequest\x1a\x18.mt4grpc.DisconnectReply2\xa2\t\n\x03MT4\x12N\n\x0eAccountSummary\x12\x1e.mt4grpc.AccountSummaryRequest\x1a\x1c.mt4grpc.AccountSummaryReply\x126\n\x06Groups\x12\x16.mt4grpc.GroupsRequest\x1a\x14.mt4grpc.GroupsReply\x123\n\x05Quote\x12\x15.mt4grpc.QuoteRequest\x1a\x13.mt4grpc.QuoteReply\x12H\n\x0cOpenedOrders\x12\x1c.mt4grpc.OpenedOrdersRequest\x1a\x1a.mt4grpc.OpenedOrdersReply\x129\n\x07Symbols\x12\x17.mt4grpc.SymbolsRequest\x1a\x15.mt4grpc.SymbolsReply\x12H\n\x0cSymbolParams\x12\x1c.mt4grpc.SymbolParamsRequest\x1a\x1a.mt4grpc.SymbolParamsReply\x12N\n\x0eServerTimezone\x12\x1e.mt4grpc.ServerTimezoneRequest\x1a\x1c.mt4grpc.ServerTimezoneReply\x12T\n\x10SymbolParamsMany\x12 .mt4grpc.SymbolParamsManyRequest\x1a\x1e.mt4grpc.SymbolParamsManyReply\x12E\n\x0bOpenedOrder\x12\x1b.mt4grpc.OpenedOrderRequest\x1a\x19.mt4grpc.OpenedOrderReply\x12H\n\x0cOrderHistory\x12\x1c.mt4grpc.OrderHistoryRequest\x1a\x1a.mt4grpc.OrderHistoryReply\x12H\n\x0cQuoteHistory\x12\x1c.mt4grpc.QuoteHistoryRequest\x1a\x1a.mt4grpc.QuoteHistoryReply\x12T\n\x10QuoteHistoryMany\x12 .mt4grpc.QuoteHistoryManyRequest\x1a\x1e.mt4grpc.QuoteHistoryManyReply\x12H\n\x0cClosedOrders\x12\x1c.mt4grpc.ClosedOrdersRequest\x1a\x1a.mt4grpc.ClosedOrdersReply\x12]\n\x13RequestQuoteHistory\x12#.mt4grpc.RequestQuoteHistoryRequest\x1a!.mt4grpc.RequestQuoteHistoryReply\x12K\n\rSetPlacedType\x12\x1d.mt4grpc.SetPlacedTypeRequest\x1a\x1b.mt4grpc.SetPlacedTypeReply\x12B\n\nIsInvestor\x12\x1a.mt4grpc.IsInvestorRequest\x1a\x18.mt4grpc.IsInvestorReply2\xd6\x03\n\x07Service\x120\n\x04Ping\x12\x14.mt4grpc.PingRequest\x1a\x12.mt4grpc.PingReply\x129\n\x07GetLogs\x12\x17.mt4grpc.GetLogsRequest\x1a\x15.mt4grpc.GetLogsReply\x12K\n\rGetLogsByUser\x12\x1d.mt4grpc.GetLogsByUserRequest\x1a\x1b.mt4grpc.GetLogsByUserReply\x12N\n\x0eMemorySnapshot\x12\x1e.mt4grpc.MemorySnapshotRequest\x1a\x1c.mt4grpc.MemorySnapshotReply\x126\n\x06Search\x12\x16.mt4grpc.SearchRequest\x1a\x14.mt4grpc.SearchReply\x12B\n\nGetClients\x12\x1a.mt4grpc.GetClientsRequest\x1a\x18.mt4grpc.GetClientsReply\x12E\n\x0bMemoryUsage\x12\x1b.mt4grpc.MemoryUsageRequest\x1a\x19.mt4grpc.MemoryUsageReply2\xbc\x05\n\rSubscriptions\x12?\n\tSubscribe\x12\x19.mt4grpc.SubscribeRequest\x1a\x17.mt4grpc.SubscribeReply\x12K\n\rSubscribeMany\x12\x1d.mt4grpc.SubscribeManyRequest\x1a\x1b.mt4grpc.SubscribeManyReply\x12E\n\x0bUnSubscribe\x12\x1b.mt4grpc.UnSubscribeRequest\x1a\x19.mt4grpc.UnSubscribeReply\x12Q\n\x0fUnSubscribeMany\x12\x1f.mt4grpc.UnSubscribeManyRequest\x1a\x1d.mt4grpc.UnSubscribeManyReply\x12`\n\x14SubscribeOrderProfit\x12$.mt4grpc.SubscribeOrderProfitRequest\x1a".mt4grpc.SubscribeOrderProfitReply\x12Z\n\x12SubscribeTickValue\x12".mt4grpc.SubscribeTickValueRequest\x1a .mt4grpc.SubscribeTickValueReply\x12`\n\x14SubscribeOrderUpdate\x12$.mt4grpc.SubscribeOrderUpdateRequest\x1a".mt4grpc.SubscribeOrderUpdateReply\x12c\n\x15SubscribeQuoteHistory\x12%.mt4grpc.SubscribeQuoteHistoryRequest\x1a#.mt4grpc.SubscribeQuoteHistoryReply2\xe6\x02\n\x07Trading\x12?\n\tOrderSend\x12\x19.mt4grpc.OrderSendRequest\x1a\x17.mt4grpc.OrderSendReply\x12E\n\x0bOrderModify\x12\x1b.mt4grpc.OrderModifyRequest\x1a\x19.mt4grpc.OrderModifyReply\x12H\n\x0cOrderCloseBy\x12\x1c.mt4grpc.OrderCloseByRequest\x1a\x1a.mt4grpc.OrderCloseByReply\x12E\n\x0bOrderDelete\x12\x1b.mt4grpc.OrderDeleteRequest\x1a\x19.mt4grpc.OrderDeleteReply\x12B\n\nOrderClose\x12\x1a.mt4grpc.OrderCloseRequest\x1a\x18.mt4grpc.OrderCloseReply2\xad\x02\n\x07Streams\x12M\n\rOnOrderUpdate\x12\x1d.mt4grpc.OnOrderUpdateRequest\x1a\x1b.mt4grpc.OnOrderUpdateReply0\x01\x12;\n\x07OnQuote\x12\x17.mt4grpc.OnQuoteRequest\x1a\x15.mt4grpc.OnQuoteReply0\x01\x12G\n\x0bOnTickValue\x12\x1b.mt4grpc.OnTickValueRequest\x1a\x19.mt4grpc.OnTickValueReply0\x01\x12M\n\rOnOrderProfit\x12\x1d.mt4grpc.OnOrderProfitRequest\x1a\x1b.mt4grpc.OnOrderProfitReply0\x01B,Z*git.gendocu.com/mtapiio/mt4grpc.git/sdk/gob\x06proto3')
_ACCOUNTTYPE = DESCRIPTOR.enum_types_by_name['AccountType']
AccountType = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE)
_PLACEDTYPE = DESCRIPTOR.enum_types_by_name['PlacedType']
PlacedType = enum_type_wrapper.EnumTypeWrapper(_PLACEDTYPE)
_OP = DESCRIPTOR.enum_types_by_name['Op']
Op = enum_type_wrapper.EnumTypeWrapper(_OP)
_EXECUTION = DESCRIPTOR.enum_types_by_name['Execution']
Execution = enum_type_wrapper.EnumTypeWrapper(_EXECUTION)
_PROFITMODE = DESCRIPTOR.enum_types_by_name['ProfitMode']
ProfitMode = enum_type_wrapper.EnumTypeWrapper(_PROFITMODE)
_MARGINMODE = DESCRIPTOR.enum_types_by_name['MarginMode']
MarginMode = enum_type_wrapper.EnumTypeWrapper(_MARGINMODE)
_TIMEFRAME = DESCRIPTOR.enum_types_by_name['Timeframe']
Timeframe = enum_type_wrapper.EnumTypeWrapper(_TIMEFRAME)
_LOGEVENTLEVEL = DESCRIPTOR.enum_types_by_name['LogEventLevel']
LogEventLevel = enum_type_wrapper.EnumTypeWrapper(_LOGEVENTLEVEL)
_UPDATEACTION = DESCRIPTOR.enum_types_by_name['UpdateAction']
UpdateAction = enum_type_wrapper.EnumTypeWrapper(_UPDATEACTION)
_ERRORCODE = DESCRIPTOR.enum_types_by_name['ErrorCode']
ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
AccountType_Real = 0
AccountType_Contest = 1
AccountType_Demo = 2
PlacedType_Client = 0
PlacedType_Expert = 1
PlacedType_Dealer = 2
PlacedType_Signal = 3
PlacedType_Gateway = 4
PlacedType_Mobile = 5
PlacedType_Web = 6
PlacedType_Api = 7
PlacedType_Default = 8
Op_Buy = 0
Op_Sell = 1
Op_BuyLimit = 2
Op_SellLimit = 3
Op_BuyStop = 4
Op_SellStop = 5
Op_Balance = 6
Op_Credit = 7
Execution_Request = 0
Execution_Instant = 1
Execution_Market = 2
ProfitMode_Forex = 0
ProfitMode_CFD = 1
ProfitMode_Futures = 2
MarginMode_Forex = 0
MarginMode_CFD = 1
MarginMode_Futures = 2
MarginMode_CfdIndex = 3
MarginMode_CfdLeverage = 4
TIMEFRAME_M0 = 0
Timeframe_M1 = 1
Timeframe_M5 = 5
Timeframe_M15 = 15
Timeframe_M30 = 30
Timeframe_H1 = 60
Timeframe_H4 = 240
Timeframe_D1 = 1440
Timeframe_W1 = 10080
Timeframe_MN1 = 43200
LogEventLevel_Verbose = 0
LogEventLevel_Debug = 1
LogEventLevel_Information = 2
LogEventLevel_Warning = 3
LogEventLevel_Error = 4
LogEventLevel_Fatal = 5
UpdateAction_PositionOpen = 0
UpdateAction_PositionClose = 1
UpdateAction_PositionModify = 2
UpdateAction_PendingOpen = 3
UpdateAction_PendingClose = 4
UpdateAction_PendingModify = 5
UpdateAction_PendingFill = 6
UpdateAction_Balance = 7
UpdateAction_Credit = 8
INTERNAL_ERROR = 0
COMMON_ERROR = 2
INVALID_PARAM = 3
SERVER_BUSY = 4
OLD_VERSION = 5
NO_CONNECT = 6
NOT_ENOUGH_RIGHTS = 7
TOO_FREQUENT_REQUEST = 8
NO_CONNECTION = 10
SERVICE_NOT_AVAILABLE = 11
TOO_FREQUENT_REQUESTS = 12
SECRET_KEY_REQUIRED = 13
INVALID_ONETIME_PASSWORD = 14
ACCOUNT_DISABLED = 64
INVALID_ACCOUNT = 65
PUBLIC_KEY_NOT_FOUND = 66
TRADE_TIMEOUT = 128
INVALID_PRICES = 129
INVALID_SL_TP = 130
INVALID_VOLUME = 131
MARKET_CLOSED = 132
TRADE_DISABLED = 133
NOT_MONEY = 134
PRICE_CHANGED = 135
OFF_QUOTES = 136
BROKER_BUSY = 137
REQUOTE = 138
ORDER_LOCKED = 139
LONG_POS_ALLOWED = 140
TOO_MANY_REQUESTS = 141
ORDER_ACCEPTED = 142
ORDER_IN_PROCESS = 143
REQUEST_CANCELLED = 144
MODIFICATIONS_DENIED = 145
TRADE_CONTEXT_BUSY = 146
EXPIRATION_DISABLED = 147
TOO_MANY_ORDERS = 148
HEDGE_PROHIBITED = 149
RPROHIBITED_FIFO = 150
INVALID_TOKEN = 256
INVALID_SYMBOL = 257
INVALID_TICKET = 258
SAME_PARAMS = 259
CONNECT_ERROR = 260
TIMEOUT = 261
_ERROR = DESCRIPTOR.message_types_by_name['Error']
_CONNECTREQUEST = DESCRIPTOR.message_types_by_name['ConnectRequest']
_CONNECTREPLY = DESCRIPTOR.message_types_by_name['ConnectReply']
_CHECKCONNECTREQUEST = DESCRIPTOR.message_types_by_name['CheckConnectRequest']
_CHECKCONNECTREPLY = DESCRIPTOR.message_types_by_name['CheckConnectReply']
_DISCONNECTREQUEST = DESCRIPTOR.message_types_by_name['DisconnectRequest']
_DISCONNECTREPLY = DESCRIPTOR.message_types_by_name['DisconnectReply']
_ACCOUNTSUMMARYREQUEST = DESCRIPTOR.message_types_by_name['AccountSummaryRequest']
_ACCOUNTSUMMARY = DESCRIPTOR.message_types_by_name['AccountSummary']
_ACCOUNTSUMMARYREPLY = DESCRIPTOR.message_types_by_name['AccountSummaryReply']
_GROUPSREQUEST = DESCRIPTOR.message_types_by_name['GroupsRequest']
_CONSYMBOLGROUP = DESCRIPTOR.message_types_by_name['ConSymbolGroup']
_GROUPSREPLY = DESCRIPTOR.message_types_by_name['GroupsReply']
_QUOTEREQUEST = DESCRIPTOR.message_types_by_name['QuoteRequest']
_QUOTEEVENTARGS = DESCRIPTOR.message_types_by_name['QuoteEventArgs']
_QUOTEREPLY = DESCRIPTOR.message_types_by_name['QuoteReply']
_OPENEDORDERSREQUEST = DESCRIPTOR.message_types_by_name['OpenedOrdersRequest']
_ORDER = DESCRIPTOR.message_types_by_name['Order']
_OPENEDORDERSREPLY = DESCRIPTOR.message_types_by_name['OpenedOrdersReply']
_SYMBOLSREQUEST = DESCRIPTOR.message_types_by_name['SymbolsRequest']
_SYMBOLSREPLY = DESCRIPTOR.message_types_by_name['SymbolsReply']
_SYMBOLPARAMSREQUEST = DESCRIPTOR.message_types_by_name['SymbolParamsRequest']
_SYMBOLPARAMS = DESCRIPTOR.message_types_by_name['SymbolParams']
_SYMBOLINFO = DESCRIPTOR.message_types_by_name['SymbolInfo']
_CONGROUPSEC = DESCRIPTOR.message_types_by_name['ConGroupSec']
_SYMBOLPARAMSREPLY = DESCRIPTOR.message_types_by_name['SymbolParamsReply']
_SERVERTIMEZONEREQUEST = DESCRIPTOR.message_types_by_name['ServerTimezoneRequest']
_SERVERTIMEZONEREPLY = DESCRIPTOR.message_types_by_name['ServerTimezoneReply']
_ISINVESTORREQUEST = DESCRIPTOR.message_types_by_name['IsInvestorRequest']
_ISINVESTORREPLY = DESCRIPTOR.message_types_by_name['IsInvestorReply']
_SYMBOLPARAMSMANYREQUEST = DESCRIPTOR.message_types_by_name['SymbolParamsManyRequest']
_SYMBOLPARAMSMANYREPLY = DESCRIPTOR.message_types_by_name['SymbolParamsManyReply']
_OPENEDORDERREQUEST = DESCRIPTOR.message_types_by_name['OpenedOrderRequest']
_OPENEDORDERREPLY = DESCRIPTOR.message_types_by_name['OpenedOrderReply']
_ORDERHISTORYREQUEST = DESCRIPTOR.message_types_by_name['OrderHistoryRequest']
_ORDERHISTORYREPLY = DESCRIPTOR.message_types_by_name['OrderHistoryReply']
_QUOTEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['QuoteHistoryRequest']
_BAR = DESCRIPTOR.message_types_by_name['Bar']
_QUOTEHISTORYREPLY = DESCRIPTOR.message_types_by_name['QuoteHistoryReply']
_QUOTEHISTORYMANYREQUEST = DESCRIPTOR.message_types_by_name['QuoteHistoryManyRequest']
_BARSFORSYMBOL = DESCRIPTOR.message_types_by_name['BarsForSymbol']
_QUOTEHISTORYMANYREPLY = DESCRIPTOR.message_types_by_name['QuoteHistoryManyReply']
_CLOSEDORDERSREQUEST = DESCRIPTOR.message_types_by_name['ClosedOrdersRequest']
_CLOSEDORDERSREPLY = DESCRIPTOR.message_types_by_name['ClosedOrdersReply']
_REQUESTQUOTEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['RequestQuoteHistoryRequest']
_REQUESTQUOTEHISTORYREPLY = DESCRIPTOR.message_types_by_name['RequestQuoteHistoryReply']
_SETPLACEDTYPEREQUEST = DESCRIPTOR.message_types_by_name['SetPlacedTypeRequest']
_SETPLACEDTYPEREPLY = DESCRIPTOR.message_types_by_name['SetPlacedTypeReply']
_PINGREQUEST = DESCRIPTOR.message_types_by_name['PingRequest']
_PINGREPLY = DESCRIPTOR.message_types_by_name['PingReply']
_GETLOGSREQUEST = DESCRIPTOR.message_types_by_name['GetLogsRequest']
_LOGREC = DESCRIPTOR.message_types_by_name['LogRec']
_GETLOGSREPLY = DESCRIPTOR.message_types_by_name['GetLogsReply']
_GETLOGSBYUSERREQUEST = DESCRIPTOR.message_types_by_name['GetLogsByUserRequest']
_GETLOGSBYUSERREPLY = DESCRIPTOR.message_types_by_name['GetLogsByUserReply']
_MEMORYSNAPSHOTREQUEST = DESCRIPTOR.message_types_by_name['MemorySnapshotRequest']
_MEMORYSNAPSHOTREPLY = DESCRIPTOR.message_types_by_name['MemorySnapshotReply']
_SEARCHREQUEST = DESCRIPTOR.message_types_by_name['SearchRequest']
_BROKERSERACHRESULT = DESCRIPTOR.message_types_by_name['BrokerSerachResult']
_BROKERCOMPANY = DESCRIPTOR.message_types_by_name['BrokerCompany']
_BROKERSERVER = DESCRIPTOR.message_types_by_name['BrokerServer']
_SEARCHREPLY = DESCRIPTOR.message_types_by_name['SearchReply']
_GETCLIENTSREQUEST = DESCRIPTOR.message_types_by_name['GetClientsRequest']
_CLIENTSTATUS = DESCRIPTOR.message_types_by_name['ClientStatus']
_GETCLIENTSREPLY = DESCRIPTOR.message_types_by_name['GetClientsReply']
_MEMORYUSAGEREQUEST = DESCRIPTOR.message_types_by_name['MemoryUsageRequest']
_MEMUSAGE = DESCRIPTOR.message_types_by_name['MemUsage']
_MEMORYUSAGEREPLY = DESCRIPTOR.message_types_by_name['MemoryUsageReply']
_SUBSCRIBEREQUEST = DESCRIPTOR.message_types_by_name['SubscribeRequest']
_SUBSCRIBEREPLY = DESCRIPTOR.message_types_by_name['SubscribeReply']
_SUBSCRIBEMANYREQUEST = DESCRIPTOR.message_types_by_name['SubscribeManyRequest']
_SUBSCRIBEMANYREPLY = DESCRIPTOR.message_types_by_name['SubscribeManyReply']
_UNSUBSCRIBEREQUEST = DESCRIPTOR.message_types_by_name['UnSubscribeRequest']
_UNSUBSCRIBEREPLY = DESCRIPTOR.message_types_by_name['UnSubscribeReply']
_UNSUBSCRIBEMANYREQUEST = DESCRIPTOR.message_types_by_name['UnSubscribeManyRequest']
_UNSUBSCRIBEMANYREPLY = DESCRIPTOR.message_types_by_name['UnSubscribeManyReply']
_SUBSCRIBEORDERPROFITREQUEST = DESCRIPTOR.message_types_by_name['SubscribeOrderProfitRequest']
_SUBSCRIBEORDERPROFITREPLY = DESCRIPTOR.message_types_by_name['SubscribeOrderProfitReply']
_SUBSCRIBETICKVALUEREQUEST = DESCRIPTOR.message_types_by_name['SubscribeTickValueRequest']
_SUBSCRIBETICKVALUEREPLY = DESCRIPTOR.message_types_by_name['SubscribeTickValueReply']
_SUBSCRIBEORDERUPDATEREQUEST = DESCRIPTOR.message_types_by_name['SubscribeOrderUpdateRequest']
_SUBSCRIBEORDERUPDATEREPLY = DESCRIPTOR.message_types_by_name['SubscribeOrderUpdateReply']
_SUBSCRIBEQUOTEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['SubscribeQuoteHistoryRequest']
_SUBSCRIBEQUOTEHISTORYREPLY = DESCRIPTOR.message_types_by_name['SubscribeQuoteHistoryReply']
_ORDERSENDREQUEST = DESCRIPTOR.message_types_by_name['OrderSendRequest']
_ORDERSENDREPLY = DESCRIPTOR.message_types_by_name['OrderSendReply']
_ORDERMODIFYREQUEST = DESCRIPTOR.message_types_by_name['OrderModifyRequest']
_ORDERMODIFYREPLY = DESCRIPTOR.message_types_by_name['OrderModifyReply']
_ORDERCLOSEBYREQUEST = DESCRIPTOR.message_types_by_name['OrderCloseByRequest']
_ORDERCLOSEBYREPLY = DESCRIPTOR.message_types_by_name['OrderCloseByReply']
_ORDERDELETEREQUEST = DESCRIPTOR.message_types_by_name['OrderDeleteRequest']
_ORDERDELETEREPLY = DESCRIPTOR.message_types_by_name['OrderDeleteReply']
_ORDERCLOSEREQUEST = DESCRIPTOR.message_types_by_name['OrderCloseRequest']
_ORDERCLOSEREPLY = DESCRIPTOR.message_types_by_name['OrderCloseReply']
_EVENTSREQUEST = DESCRIPTOR.message_types_by_name['EventsRequest']
_EVENTSREPLY = DESCRIPTOR.message_types_by_name['EventsReply']
_ONORDERUPDATEREQUEST = DESCRIPTOR.message_types_by_name['OnOrderUpdateRequest']
_ORDERUPDATESUMMARY = DESCRIPTOR.message_types_by_name['OrderUpdateSummary']
_ORDERUPDATEEVENTARGS = DESCRIPTOR.message_types_by_name['OrderUpdateEventArgs']
_ONORDERUPDATEREPLY = DESCRIPTOR.message_types_by_name['OnOrderUpdateReply']
_ONQUOTEREQUEST = DESCRIPTOR.message_types_by_name['OnQuoteRequest']
_ONQUOTEREPLY = DESCRIPTOR.message_types_by_name['OnQuoteReply']
_ONTICKVALUEREQUEST = DESCRIPTOR.message_types_by_name['OnTickValueRequest']
_SYMBOLTICKVALUE = DESCRIPTOR.message_types_by_name['SymbolTickValue']
_ONTICKVALUEREPLY = DESCRIPTOR.message_types_by_name['OnTickValueReply']
_ONORDERPROFITREQUEST = DESCRIPTOR.message_types_by_name['OnOrderProfitRequest']
_PROFITUPDATE = DESCRIPTOR.message_types_by_name['ProfitUpdate']
_ONORDERPROFITREPLY = DESCRIPTOR.message_types_by_name['OnOrderProfitReply']
_ONQUOTEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['OnQuoteHistoryRequest']
_QUOTEHISTORYEVENTARGS = DESCRIPTOR.message_types_by_name['QuoteHistoryEventArgs']
_ONQUOTEHISTORYREPLY = DESCRIPTOR.message_types_by_name['OnQuoteHistoryReply']
_ONDISCONNECTREQUEST = DESCRIPTOR.message_types_by_name['OnDisconnectRequest']
_ONDISCONNECTREPLY = DESCRIPTOR.message_types_by_name['OnDisconnectReply']
Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {'DESCRIPTOR': _ERROR, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(Error)
ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), {'DESCRIPTOR': _CONNECTREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ConnectRequest)
ConnectReply = _reflection.GeneratedProtocolMessageType('ConnectReply', (_message.Message,), {'DESCRIPTOR': _CONNECTREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ConnectReply)
CheckConnectRequest = _reflection.GeneratedProtocolMessageType('CheckConnectRequest', (_message.Message,), {'DESCRIPTOR': _CHECKCONNECTREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(CheckConnectRequest)
CheckConnectReply = _reflection.GeneratedProtocolMessageType('CheckConnectReply', (_message.Message,), {'DESCRIPTOR': _CHECKCONNECTREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(CheckConnectReply)
DisconnectRequest = _reflection.GeneratedProtocolMessageType('DisconnectRequest', (_message.Message,), {'DESCRIPTOR': _DISCONNECTREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(DisconnectRequest)
DisconnectReply = _reflection.GeneratedProtocolMessageType('DisconnectReply', (_message.Message,), {'DESCRIPTOR': _DISCONNECTREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(DisconnectReply)
AccountSummaryRequest = _reflection.GeneratedProtocolMessageType('AccountSummaryRequest', (_message.Message,), {'DESCRIPTOR': _ACCOUNTSUMMARYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(AccountSummaryRequest)
AccountSummary = _reflection.GeneratedProtocolMessageType('AccountSummary', (_message.Message,), {'DESCRIPTOR': _ACCOUNTSUMMARY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(AccountSummary)
AccountSummaryReply = _reflection.GeneratedProtocolMessageType('AccountSummaryReply', (_message.Message,), {'DESCRIPTOR': _ACCOUNTSUMMARYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(AccountSummaryReply)
GroupsRequest = _reflection.GeneratedProtocolMessageType('GroupsRequest', (_message.Message,), {'DESCRIPTOR': _GROUPSREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(GroupsRequest)
ConSymbolGroup = _reflection.GeneratedProtocolMessageType('ConSymbolGroup', (_message.Message,), {'DESCRIPTOR': _CONSYMBOLGROUP, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ConSymbolGroup)
GroupsReply = _reflection.GeneratedProtocolMessageType('GroupsReply', (_message.Message,), {'DESCRIPTOR': _GROUPSREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(GroupsReply)
QuoteRequest = _reflection.GeneratedProtocolMessageType('QuoteRequest', (_message.Message,), {'DESCRIPTOR': _QUOTEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(QuoteRequest)
QuoteEventArgs = _reflection.GeneratedProtocolMessageType('QuoteEventArgs', (_message.Message,), {'DESCRIPTOR': _QUOTEEVENTARGS, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(QuoteEventArgs)
QuoteReply = _reflection.GeneratedProtocolMessageType('QuoteReply', (_message.Message,), {'DESCRIPTOR': _QUOTEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(QuoteReply)
OpenedOrdersRequest = _reflection.GeneratedProtocolMessageType('OpenedOrdersRequest', (_message.Message,), {'DESCRIPTOR': _OPENEDORDERSREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OpenedOrdersRequest)
Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {'DESCRIPTOR': _ORDER, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(Order)
OpenedOrdersReply = _reflection.GeneratedProtocolMessageType('OpenedOrdersReply', (_message.Message,), {'DESCRIPTOR': _OPENEDORDERSREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OpenedOrdersReply)
SymbolsRequest = _reflection.GeneratedProtocolMessageType('SymbolsRequest', (_message.Message,), {'DESCRIPTOR': _SYMBOLSREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolsRequest)
SymbolsReply = _reflection.GeneratedProtocolMessageType('SymbolsReply', (_message.Message,), {'DESCRIPTOR': _SYMBOLSREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolsReply)
SymbolParamsRequest = _reflection.GeneratedProtocolMessageType('SymbolParamsRequest', (_message.Message,), {'DESCRIPTOR': _SYMBOLPARAMSREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolParamsRequest)
SymbolParams = _reflection.GeneratedProtocolMessageType('SymbolParams', (_message.Message,), {'DESCRIPTOR': _SYMBOLPARAMS, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolParams)
SymbolInfo = _reflection.GeneratedProtocolMessageType('SymbolInfo', (_message.Message,), {'DESCRIPTOR': _SYMBOLINFO, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolInfo)
ConGroupSec = _reflection.GeneratedProtocolMessageType('ConGroupSec', (_message.Message,), {'DESCRIPTOR': _CONGROUPSEC, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ConGroupSec)
SymbolParamsReply = _reflection.GeneratedProtocolMessageType('SymbolParamsReply', (_message.Message,), {'DESCRIPTOR': _SYMBOLPARAMSREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolParamsReply)
ServerTimezoneRequest = _reflection.GeneratedProtocolMessageType('ServerTimezoneRequest', (_message.Message,), {'DESCRIPTOR': _SERVERTIMEZONEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ServerTimezoneRequest)
ServerTimezoneReply = _reflection.GeneratedProtocolMessageType('ServerTimezoneReply', (_message.Message,), {'DESCRIPTOR': _SERVERTIMEZONEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ServerTimezoneReply)
IsInvestorRequest = _reflection.GeneratedProtocolMessageType('IsInvestorRequest', (_message.Message,), {'DESCRIPTOR': _ISINVESTORREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(IsInvestorRequest)
IsInvestorReply = _reflection.GeneratedProtocolMessageType('IsInvestorReply', (_message.Message,), {'DESCRIPTOR': _ISINVESTORREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(IsInvestorReply)
SymbolParamsManyRequest = _reflection.GeneratedProtocolMessageType('SymbolParamsManyRequest', (_message.Message,), {'DESCRIPTOR': _SYMBOLPARAMSMANYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolParamsManyRequest)
SymbolParamsManyReply = _reflection.GeneratedProtocolMessageType('SymbolParamsManyReply', (_message.Message,), {'DESCRIPTOR': _SYMBOLPARAMSMANYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolParamsManyReply)
OpenedOrderRequest = _reflection.GeneratedProtocolMessageType('OpenedOrderRequest', (_message.Message,), {'DESCRIPTOR': _OPENEDORDERREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OpenedOrderRequest)
OpenedOrderReply = _reflection.GeneratedProtocolMessageType('OpenedOrderReply', (_message.Message,), {'DESCRIPTOR': _OPENEDORDERREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OpenedOrderReply)
OrderHistoryRequest = _reflection.GeneratedProtocolMessageType('OrderHistoryRequest', (_message.Message,), {'DESCRIPTOR': _ORDERHISTORYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderHistoryRequest)
OrderHistoryReply = _reflection.GeneratedProtocolMessageType('OrderHistoryReply', (_message.Message,), {'DESCRIPTOR': _ORDERHISTORYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderHistoryReply)
QuoteHistoryRequest = _reflection.GeneratedProtocolMessageType('QuoteHistoryRequest', (_message.Message,), {'DESCRIPTOR': _QUOTEHISTORYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(QuoteHistoryRequest)
Bar = _reflection.GeneratedProtocolMessageType('Bar', (_message.Message,), {'DESCRIPTOR': _BAR, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(Bar)
QuoteHistoryReply = _reflection.GeneratedProtocolMessageType('QuoteHistoryReply', (_message.Message,), {'DESCRIPTOR': _QUOTEHISTORYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(QuoteHistoryReply)
QuoteHistoryManyRequest = _reflection.GeneratedProtocolMessageType('QuoteHistoryManyRequest', (_message.Message,), {'DESCRIPTOR': _QUOTEHISTORYMANYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(QuoteHistoryManyRequest)
BarsForSymbol = _reflection.GeneratedProtocolMessageType('BarsForSymbol', (_message.Message,), {'DESCRIPTOR': _BARSFORSYMBOL, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(BarsForSymbol)
QuoteHistoryManyReply = _reflection.GeneratedProtocolMessageType('QuoteHistoryManyReply', (_message.Message,), {'DESCRIPTOR': _QUOTEHISTORYMANYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(QuoteHistoryManyReply)
ClosedOrdersRequest = _reflection.GeneratedProtocolMessageType('ClosedOrdersRequest', (_message.Message,), {'DESCRIPTOR': _CLOSEDORDERSREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ClosedOrdersRequest)
ClosedOrdersReply = _reflection.GeneratedProtocolMessageType('ClosedOrdersReply', (_message.Message,), {'DESCRIPTOR': _CLOSEDORDERSREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ClosedOrdersReply)
RequestQuoteHistoryRequest = _reflection.GeneratedProtocolMessageType('RequestQuoteHistoryRequest', (_message.Message,), {'DESCRIPTOR': _REQUESTQUOTEHISTORYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(RequestQuoteHistoryRequest)
RequestQuoteHistoryReply = _reflection.GeneratedProtocolMessageType('RequestQuoteHistoryReply', (_message.Message,), {'DESCRIPTOR': _REQUESTQUOTEHISTORYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(RequestQuoteHistoryReply)
SetPlacedTypeRequest = _reflection.GeneratedProtocolMessageType('SetPlacedTypeRequest', (_message.Message,), {'DESCRIPTOR': _SETPLACEDTYPEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SetPlacedTypeRequest)
SetPlacedTypeReply = _reflection.GeneratedProtocolMessageType('SetPlacedTypeReply', (_message.Message,), {'DESCRIPTOR': _SETPLACEDTYPEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SetPlacedTypeReply)
PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {'DESCRIPTOR': _PINGREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(PingRequest)
PingReply = _reflection.GeneratedProtocolMessageType('PingReply', (_message.Message,), {'DESCRIPTOR': _PINGREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(PingReply)
GetLogsRequest = _reflection.GeneratedProtocolMessageType('GetLogsRequest', (_message.Message,), {'DESCRIPTOR': _GETLOGSREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(GetLogsRequest)
LogRec = _reflection.GeneratedProtocolMessageType('LogRec', (_message.Message,), {'DESCRIPTOR': _LOGREC, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(LogRec)
GetLogsReply = _reflection.GeneratedProtocolMessageType('GetLogsReply', (_message.Message,), {'DESCRIPTOR': _GETLOGSREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(GetLogsReply)
GetLogsByUserRequest = _reflection.GeneratedProtocolMessageType('GetLogsByUserRequest', (_message.Message,), {'DESCRIPTOR': _GETLOGSBYUSERREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(GetLogsByUserRequest)
GetLogsByUserReply = _reflection.GeneratedProtocolMessageType('GetLogsByUserReply', (_message.Message,), {'DESCRIPTOR': _GETLOGSBYUSERREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(GetLogsByUserReply)
MemorySnapshotRequest = _reflection.GeneratedProtocolMessageType('MemorySnapshotRequest', (_message.Message,), {'DESCRIPTOR': _MEMORYSNAPSHOTREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(MemorySnapshotRequest)
MemorySnapshotReply = _reflection.GeneratedProtocolMessageType('MemorySnapshotReply', (_message.Message,), {'DESCRIPTOR': _MEMORYSNAPSHOTREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(MemorySnapshotReply)
SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {'DESCRIPTOR': _SEARCHREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SearchRequest)
BrokerSerachResult = _reflection.GeneratedProtocolMessageType('BrokerSerachResult', (_message.Message,), {'DESCRIPTOR': _BROKERSERACHRESULT, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(BrokerSerachResult)
BrokerCompany = _reflection.GeneratedProtocolMessageType('BrokerCompany', (_message.Message,), {'DESCRIPTOR': _BROKERCOMPANY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(BrokerCompany)
BrokerServer = _reflection.GeneratedProtocolMessageType('BrokerServer', (_message.Message,), {'DESCRIPTOR': _BROKERSERVER, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(BrokerServer)
SearchReply = _reflection.GeneratedProtocolMessageType('SearchReply', (_message.Message,), {'DESCRIPTOR': _SEARCHREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SearchReply)
GetClientsRequest = _reflection.GeneratedProtocolMessageType('GetClientsRequest', (_message.Message,), {'DESCRIPTOR': _GETCLIENTSREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(GetClientsRequest)
ClientStatus = _reflection.GeneratedProtocolMessageType('ClientStatus', (_message.Message,), {'DESCRIPTOR': _CLIENTSTATUS, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ClientStatus)
GetClientsReply = _reflection.GeneratedProtocolMessageType('GetClientsReply', (_message.Message,), {'DESCRIPTOR': _GETCLIENTSREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(GetClientsReply)
MemoryUsageRequest = _reflection.GeneratedProtocolMessageType('MemoryUsageRequest', (_message.Message,), {'DESCRIPTOR': _MEMORYUSAGEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(MemoryUsageRequest)
MemUsage = _reflection.GeneratedProtocolMessageType('MemUsage', (_message.Message,), {'DESCRIPTOR': _MEMUSAGE, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(MemUsage)
MemoryUsageReply = _reflection.GeneratedProtocolMessageType('MemoryUsageReply', (_message.Message,), {'DESCRIPTOR': _MEMORYUSAGEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(MemoryUsageReply)
SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeRequest)
SubscribeReply = _reflection.GeneratedProtocolMessageType('SubscribeReply', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeReply)
SubscribeManyRequest = _reflection.GeneratedProtocolMessageType('SubscribeManyRequest', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEMANYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeManyRequest)
SubscribeManyReply = _reflection.GeneratedProtocolMessageType('SubscribeManyReply', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEMANYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeManyReply)
UnSubscribeRequest = _reflection.GeneratedProtocolMessageType('UnSubscribeRequest', (_message.Message,), {'DESCRIPTOR': _UNSUBSCRIBEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(UnSubscribeRequest)
UnSubscribeReply = _reflection.GeneratedProtocolMessageType('UnSubscribeReply', (_message.Message,), {'DESCRIPTOR': _UNSUBSCRIBEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(UnSubscribeReply)
UnSubscribeManyRequest = _reflection.GeneratedProtocolMessageType('UnSubscribeManyRequest', (_message.Message,), {'DESCRIPTOR': _UNSUBSCRIBEMANYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(UnSubscribeManyRequest)
UnSubscribeManyReply = _reflection.GeneratedProtocolMessageType('UnSubscribeManyReply', (_message.Message,), {'DESCRIPTOR': _UNSUBSCRIBEMANYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(UnSubscribeManyReply)
SubscribeOrderProfitRequest = _reflection.GeneratedProtocolMessageType('SubscribeOrderProfitRequest', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEORDERPROFITREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeOrderProfitRequest)
SubscribeOrderProfitReply = _reflection.GeneratedProtocolMessageType('SubscribeOrderProfitReply', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEORDERPROFITREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeOrderProfitReply)
SubscribeTickValueRequest = _reflection.GeneratedProtocolMessageType('SubscribeTickValueRequest', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBETICKVALUEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeTickValueRequest)
SubscribeTickValueReply = _reflection.GeneratedProtocolMessageType('SubscribeTickValueReply', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBETICKVALUEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeTickValueReply)
SubscribeOrderUpdateRequest = _reflection.GeneratedProtocolMessageType('SubscribeOrderUpdateRequest', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEORDERUPDATEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeOrderUpdateRequest)
SubscribeOrderUpdateReply = _reflection.GeneratedProtocolMessageType('SubscribeOrderUpdateReply', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEORDERUPDATEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeOrderUpdateReply)
SubscribeQuoteHistoryRequest = _reflection.GeneratedProtocolMessageType('SubscribeQuoteHistoryRequest', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEQUOTEHISTORYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeQuoteHistoryRequest)
SubscribeQuoteHistoryReply = _reflection.GeneratedProtocolMessageType('SubscribeQuoteHistoryReply', (_message.Message,), {'DESCRIPTOR': _SUBSCRIBEQUOTEHISTORYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SubscribeQuoteHistoryReply)
OrderSendRequest = _reflection.GeneratedProtocolMessageType('OrderSendRequest', (_message.Message,), {'DESCRIPTOR': _ORDERSENDREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderSendRequest)
OrderSendReply = _reflection.GeneratedProtocolMessageType('OrderSendReply', (_message.Message,), {'DESCRIPTOR': _ORDERSENDREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderSendReply)
OrderModifyRequest = _reflection.GeneratedProtocolMessageType('OrderModifyRequest', (_message.Message,), {'DESCRIPTOR': _ORDERMODIFYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderModifyRequest)
OrderModifyReply = _reflection.GeneratedProtocolMessageType('OrderModifyReply', (_message.Message,), {'DESCRIPTOR': _ORDERMODIFYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderModifyReply)
OrderCloseByRequest = _reflection.GeneratedProtocolMessageType('OrderCloseByRequest', (_message.Message,), {'DESCRIPTOR': _ORDERCLOSEBYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderCloseByRequest)
OrderCloseByReply = _reflection.GeneratedProtocolMessageType('OrderCloseByReply', (_message.Message,), {'DESCRIPTOR': _ORDERCLOSEBYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderCloseByReply)
OrderDeleteRequest = _reflection.GeneratedProtocolMessageType('OrderDeleteRequest', (_message.Message,), {'DESCRIPTOR': _ORDERDELETEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderDeleteRequest)
OrderDeleteReply = _reflection.GeneratedProtocolMessageType('OrderDeleteReply', (_message.Message,), {'DESCRIPTOR': _ORDERDELETEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderDeleteReply)
OrderCloseRequest = _reflection.GeneratedProtocolMessageType('OrderCloseRequest', (_message.Message,), {'DESCRIPTOR': _ORDERCLOSEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderCloseRequest)
OrderCloseReply = _reflection.GeneratedProtocolMessageType('OrderCloseReply', (_message.Message,), {'DESCRIPTOR': _ORDERCLOSEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderCloseReply)
EventsRequest = _reflection.GeneratedProtocolMessageType('EventsRequest', (_message.Message,), {'DESCRIPTOR': _EVENTSREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(EventsRequest)
EventsReply = _reflection.GeneratedProtocolMessageType('EventsReply', (_message.Message,), {'DESCRIPTOR': _EVENTSREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(EventsReply)
OnOrderUpdateRequest = _reflection.GeneratedProtocolMessageType('OnOrderUpdateRequest', (_message.Message,), {'DESCRIPTOR': _ONORDERUPDATEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnOrderUpdateRequest)
OrderUpdateSummary = _reflection.GeneratedProtocolMessageType('OrderUpdateSummary', (_message.Message,), {'DESCRIPTOR': _ORDERUPDATESUMMARY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderUpdateSummary)
OrderUpdateEventArgs = _reflection.GeneratedProtocolMessageType('OrderUpdateEventArgs', (_message.Message,), {'DESCRIPTOR': _ORDERUPDATEEVENTARGS, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OrderUpdateEventArgs)
OnOrderUpdateReply = _reflection.GeneratedProtocolMessageType('OnOrderUpdateReply', (_message.Message,), {'DESCRIPTOR': _ONORDERUPDATEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnOrderUpdateReply)
OnQuoteRequest = _reflection.GeneratedProtocolMessageType('OnQuoteRequest', (_message.Message,), {'DESCRIPTOR': _ONQUOTEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnQuoteRequest)
OnQuoteReply = _reflection.GeneratedProtocolMessageType('OnQuoteReply', (_message.Message,), {'DESCRIPTOR': _ONQUOTEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnQuoteReply)
OnTickValueRequest = _reflection.GeneratedProtocolMessageType('OnTickValueRequest', (_message.Message,), {'DESCRIPTOR': _ONTICKVALUEREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnTickValueRequest)
SymbolTickValue = _reflection.GeneratedProtocolMessageType('SymbolTickValue', (_message.Message,), {'DESCRIPTOR': _SYMBOLTICKVALUE, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(SymbolTickValue)
OnTickValueReply = _reflection.GeneratedProtocolMessageType('OnTickValueReply', (_message.Message,), {'DESCRIPTOR': _ONTICKVALUEREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnTickValueReply)
OnOrderProfitRequest = _reflection.GeneratedProtocolMessageType('OnOrderProfitRequest', (_message.Message,), {'DESCRIPTOR': _ONORDERPROFITREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnOrderProfitRequest)
ProfitUpdate = _reflection.GeneratedProtocolMessageType('ProfitUpdate', (_message.Message,), {'DESCRIPTOR': _PROFITUPDATE, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(ProfitUpdate)
OnOrderProfitReply = _reflection.GeneratedProtocolMessageType('OnOrderProfitReply', (_message.Message,), {'DESCRIPTOR': _ONORDERPROFITREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnOrderProfitReply)
OnQuoteHistoryRequest = _reflection.GeneratedProtocolMessageType('OnQuoteHistoryRequest', (_message.Message,), {'DESCRIPTOR': _ONQUOTEHISTORYREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnQuoteHistoryRequest)
QuoteHistoryEventArgs = _reflection.GeneratedProtocolMessageType('QuoteHistoryEventArgs', (_message.Message,), {'DESCRIPTOR': _QUOTEHISTORYEVENTARGS, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(QuoteHistoryEventArgs)
OnQuoteHistoryReply = _reflection.GeneratedProtocolMessageType('OnQuoteHistoryReply', (_message.Message,), {'DESCRIPTOR': _ONQUOTEHISTORYREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnQuoteHistoryReply)
OnDisconnectRequest = _reflection.GeneratedProtocolMessageType('OnDisconnectRequest', (_message.Message,), {'DESCRIPTOR': _ONDISCONNECTREQUEST, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnDisconnectRequest)
OnDisconnectReply = _reflection.GeneratedProtocolMessageType('OnDisconnectReply', (_message.Message,), {'DESCRIPTOR': _ONDISCONNECTREPLY, '__module__': 'mt4_pb2'})
_sym_db.RegisterMessage(OnDisconnectReply)
_CONNECTION = DESCRIPTOR.services_by_name['Connection']
_MT4 = DESCRIPTOR.services_by_name['MT4']
_SERVICE = DESCRIPTOR.services_by_name['Service']
_SUBSCRIPTIONS = DESCRIPTOR.services_by_name['Subscriptions']
_TRADING = DESCRIPTOR.services_by_name['Trading']
_STREAMS = DESCRIPTOR.services_by_name['Streams']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z*git.gendocu.com/mtapiio/mt4grpc.git/sdk/go'
    _ACCOUNTTYPE._serialized_start = 9989
    _ACCOUNTTYPE._serialized_end = 10071
    _PLACEDTYPE._serialized_start = 10074
    _PLACEDTYPE._serialized_end = 10289
    _OP._serialized_start = 10292
    _OP._serialized_end = 10420
    _EXECUTION._serialized_start = 10422
    _EXECUTION._serialized_end = 10501
    _PROFITMODE._serialized_start = 10503
    _PROFITMODE._serialized_end = 10581
    _MARGINMODE._serialized_start = 10584
    _MARGINMODE._serialized_end = 10715
    _TIMEFRAME._serialized_start = 10718
    _TIMEFRAME._serialized_end = 10917
    _LOGEVENTLEVEL._serialized_start = 10920
    _LOGEVENTLEVEL._serialized_end = 11095
    _UPDATEACTION._serialized_start = 11098
    _UPDATEACTION._serialized_end = 11382
    _ERRORCODE._serialized_start = 11385
    _ERRORCODE._serialized_end = 12351
    _ERROR._serialized_start = 55
    _ERROR._serialized_end = 133
    _CONNECTREQUEST._serialized_start = 135
    _CONNECTREQUEST._serialized_end = 211
    _CONNECTREPLY._serialized_start = 213
    _CONNECTREPLY._serialized_end = 274
    _CHECKCONNECTREQUEST._serialized_start = 276
    _CHECKCONNECTREQUEST._serialized_end = 309
    _CHECKCONNECTREPLY._serialized_start = 311
    _CHECKCONNECTREPLY._serialized_end = 377
    _DISCONNECTREQUEST._serialized_start = 379
    _DISCONNECTREQUEST._serialized_end = 410
    _DISCONNECTREPLY._serialized_start = 412
    _DISCONNECTREPLY._serialized_end = 476
    _ACCOUNTSUMMARYREQUEST._serialized_start = 478
    _ACCOUNTSUMMARYREQUEST._serialized_end = 513
    _ACCOUNTSUMMARY._serialized_start = 516
    _ACCOUNTSUMMARY._serialized_end = 746
    _ACCOUNTSUMMARYREPLY._serialized_start = 748
    _ACCOUNTSUMMARYREPLY._serialized_end = 841
    _GROUPSREQUEST._serialized_start = 843
    _GROUPSREQUEST._serialized_end = 870
    _CONSYMBOLGROUP._serialized_start = 872
    _CONSYMBOLGROUP._serialized_end = 923
    _GROUPSREPLY._serialized_start = 925
    _GROUPSREPLY._serialized_end = 1010
    _QUOTEREQUEST._serialized_start = 1012
    _QUOTEREQUEST._serialized_end = 1054
    _QUOTEEVENTARGS._serialized_start = 1056
    _QUOTEEVENTARGS._serialized_end = 1183
    _QUOTEREPLY._serialized_start = 1185
    _QUOTEREPLY._serialized_end = 1269
    _OPENEDORDERSREQUEST._serialized_start = 1271
    _OPENEDORDERSREQUEST._serialized_end = 1304
    _ORDER._serialized_start = 1307
    _ORDER._serialized_end = 1791
    _OPENEDORDERSREPLY._serialized_start = 1793
    _OPENEDORDERSREPLY._serialized_end = 1875
    _SYMBOLSREQUEST._serialized_start = 1877
    _SYMBOLSREQUEST._serialized_end = 1905
    _SYMBOLSREPLY._serialized_start = 1907
    _SYMBOLSREPLY._serialized_end = 1968
    _SYMBOLPARAMSREQUEST._serialized_start = 1970
    _SYMBOLPARAMSREQUEST._serialized_end = 2019
    _SYMBOLPARAMS._serialized_start = 2022
    _SYMBOLPARAMS._serialized_end = 2176
    _SYMBOLINFO._serialized_start = 2179
    _SYMBOLINFO._serialized_end = 2538
    _CONGROUPSEC._serialized_start = 2541
    _CONGROUPSEC._serialized_end = 3010
    _SYMBOLPARAMSREPLY._serialized_start = 3012
    _SYMBOLPARAMSREPLY._serialized_end = 3101
    _SERVERTIMEZONEREQUEST._serialized_start = 3103
    _SERVERTIMEZONEREQUEST._serialized_end = 3138
    _SERVERTIMEZONEREPLY._serialized_start = 3140
    _SERVERTIMEZONEREPLY._serialized_end = 3208
    _ISINVESTORREQUEST._serialized_start = 3210
    _ISINVESTORREQUEST._serialized_end = 3241
    _ISINVESTORREPLY._serialized_start = 3243
    _ISINVESTORREPLY._serialized_end = 3307
    _SYMBOLPARAMSMANYREQUEST._serialized_start = 3309
    _SYMBOLPARAMSMANYREQUEST._serialized_end = 3363
    _SYMBOLPARAMSMANYREPLY._serialized_start = 3365
    _SYMBOLPARAMSMANYREPLY._serialized_end = 3458
    _OPENEDORDERREQUEST._serialized_start = 3460
    _OPENEDORDERREQUEST._serialized_end = 3508
    _OPENEDORDERREPLY._serialized_start = 3510
    _OPENEDORDERREPLY._serialized_end = 3591
    _ORDERHISTORYREQUEST._serialized_start = 3593
    _ORDERHISTORYREQUEST._serialized_end = 3652
    _ORDERHISTORYREPLY._serialized_start = 3654
    _ORDERHISTORYREPLY._serialized_end = 3736
    _QUOTEHISTORYREQUEST._serialized_start = 3738
    _QUOTEHISTORYREQUEST._serialized_end = 3855
    _BAR._serialized_start = 3857
    _BAR._serialized_end = 3976
    _QUOTEHISTORYREPLY._serialized_start = 3978
    _QUOTEHISTORYREPLY._serialized_end = 4058
    _QUOTEHISTORYMANYREQUEST._serialized_start = 4060
    _QUOTEHISTORYMANYREQUEST._serialized_end = 4181
    _BARSFORSYMBOL._serialized_start = 4183
    _BARSFORSYMBOL._serialized_end = 4261
    _QUOTEHISTORYMANYREPLY._serialized_start = 4263
    _QUOTEHISTORYMANYREPLY._serialized_end = 4357
    _CLOSEDORDERSREQUEST._serialized_start = 4359
    _CLOSEDORDERSREQUEST._serialized_end = 4392
    _CLOSEDORDERSREPLY._serialized_start = 4394
    _CLOSEDORDERSREPLY._serialized_end = 4476
    _REQUESTQUOTEHISTORYREQUEST._serialized_start = 4478
    _REQUESTQUOTEHISTORYREQUEST._serialized_end = 4602
    _REQUESTQUOTEHISTORYREPLY._serialized_start = 4604
    _REQUESTQUOTEHISTORYREPLY._serialized_end = 4677
    _SETPLACEDTYPEREQUEST._serialized_start = 4679
    _SETPLACEDTYPEREQUEST._serialized_end = 4748
    _SETPLACEDTYPEREPLY._serialized_start = 4750
    _SETPLACEDTYPEREPLY._serialized_end = 4833
    _PINGREQUEST._serialized_start = 4835
    _PINGREQUEST._serialized_end = 4848
    _PINGREPLY._serialized_start = 4850
    _PINGREPLY._serialized_end = 4908
    _GETLOGSREQUEST._serialized_start = 4910
    _GETLOGSREQUEST._serialized_end = 4938
    _LOGREC._serialized_start = 4941
    _LOGREC._serialized_end = 5091
    _GETLOGSREPLY._serialized_start = 5093
    _GETLOGSREPLY._serialized_end = 5171
    _GETLOGSBYUSERREQUEST._serialized_start = 5173
    _GETLOGSBYUSERREQUEST._serialized_end = 5227
    _GETLOGSBYUSERREPLY._serialized_start = 5229
    _GETLOGSBYUSERREPLY._serialized_end = 5313
    _MEMORYSNAPSHOTREQUEST._serialized_start = 5315
    _MEMORYSNAPSHOTREQUEST._serialized_end = 5338
    _MEMORYSNAPSHOTREPLY._serialized_start = 5340
    _MEMORYSNAPSHOTREPLY._serialized_end = 5408
    _SEARCHREQUEST._serialized_start = 5410
    _SEARCHREQUEST._serialized_end = 5442
    _BROKERSERACHRESULT._serialized_start = 5444
    _BROKERSERACHRESULT._serialized_end = 5504
    _BROKERCOMPANY._serialized_start = 5506
    _BROKERCOMPANY._serialized_end = 5578
    _BROKERSERVER._serialized_start = 5580
    _BROKERSERVER._serialized_end = 5641
    _SEARCHREPLY._serialized_start = 5643
    _SEARCHREPLY._serialized_end = 5732
    _GETCLIENTSREQUEST._serialized_start = 5734
    _GETCLIENTSREQUEST._serialized_end = 5753
    _CLIENTSTATUS._serialized_start = 5755
    _CLIENTSTATUS._serialized_end = 5842
    _GETCLIENTSREPLY._serialized_start = 5844
    _GETCLIENTSREPLY._serialized_end = 5931
    _MEMORYUSAGEREQUEST._serialized_start = 5933
    _MEMORYUSAGEREQUEST._serialized_end = 5953
    _MEMUSAGE._serialized_start = 5956
    _MEMUSAGE._serialized_end = 6444
    _MEMORYUSAGEREPLY._serialized_start = 6446
    _MEMORYUSAGEREPLY._serialized_end = 6530
    _SUBSCRIBEREQUEST._serialized_start = 6532
    _SUBSCRIBEREQUEST._serialized_end = 6596
    _SUBSCRIBEREPLY._serialized_start = 6598
    _SUBSCRIBEREPLY._serialized_end = 6661
    _SUBSCRIBEMANYREQUEST._serialized_start = 6663
    _SUBSCRIBEMANYREQUEST._serialized_end = 6732
    _SUBSCRIBEMANYREPLY._serialized_start = 6734
    _SUBSCRIBEMANYREPLY._serialized_end = 6801
    _UNSUBSCRIBEREQUEST._serialized_start = 6803
    _UNSUBSCRIBEREQUEST._serialized_end = 6851
    _UNSUBSCRIBEREPLY._serialized_start = 6853
    _UNSUBSCRIBEREPLY._serialized_end = 6918
    _UNSUBSCRIBEMANYREQUEST._serialized_start = 6920
    _UNSUBSCRIBEMANYREQUEST._serialized_end = 6973
    _UNSUBSCRIBEMANYREPLY._serialized_start = 6975
    _UNSUBSCRIBEMANYREPLY._serialized_end = 7044
    _SUBSCRIBEORDERPROFITREQUEST._serialized_start = 7046
    _SUBSCRIBEORDERPROFITREQUEST._serialized_end = 7087
    _SUBSCRIBEORDERPROFITREPLY._serialized_start = 7089
    _SUBSCRIBEORDERPROFITREPLY._serialized_end = 7179
    _SUBSCRIBETICKVALUEREQUEST._serialized_start = 7181
    _SUBSCRIBETICKVALUEREQUEST._serialized_end = 7254
    _SUBSCRIBETICKVALUEREPLY._serialized_start = 7256
    _SUBSCRIBETICKVALUEREPLY._serialized_end = 7328
    _SUBSCRIBEORDERUPDATEREQUEST._serialized_start = 7330
    _SUBSCRIBEORDERUPDATEREQUEST._serialized_end = 7371
    _SUBSCRIBEORDERUPDATEREPLY._serialized_start = 7373
    _SUBSCRIBEORDERUPDATEREPLY._serialized_end = 7463
    _SUBSCRIBEQUOTEHISTORYREQUEST._serialized_start = 7465
    _SUBSCRIBEQUOTEHISTORYREQUEST._serialized_end = 7507
    _SUBSCRIBEQUOTEHISTORYREPLY._serialized_start = 7509
    _SUBSCRIBEQUOTEHISTORYREPLY._serialized_end = 7584
    _ORDERSENDREQUEST._serialized_start = 7587
    _ORDERSENDREQUEST._serialized_end = 7845
    _ORDERSENDREPLY._serialized_start = 7847
    _ORDERSENDREPLY._serialized_end = 7926
    _ORDERMODIFYREQUEST._serialized_start = 7928
    _ORDERMODIFYREQUEST._serialized_end = 8049
    _ORDERMODIFYREPLY._serialized_start = 8051
    _ORDERMODIFYREPLY._serialized_end = 8132
    _ORDERCLOSEBYREQUEST._serialized_start = 8134
    _ORDERCLOSEBYREQUEST._serialized_end = 8201
    _ORDERCLOSEBYREPLY._serialized_start = 8203
    _ORDERCLOSEBYREPLY._serialized_end = 8269
    _ORDERDELETEREQUEST._serialized_start = 8271
    _ORDERDELETEREQUEST._serialized_end = 8319
    _ORDERDELETEREPLY._serialized_start = 8321
    _ORDERDELETEREPLY._serialized_end = 8386
    _ORDERCLOSEREQUEST._serialized_start = 8388
    _ORDERCLOSEREQUEST._serialized_end = 8482
    _ORDERCLOSEREPLY._serialized_start = 8484
    _ORDERCLOSEREPLY._serialized_end = 8564
    _EVENTSREQUEST._serialized_start = 8566
    _EVENTSREQUEST._serialized_end = 8593
    _EVENTSREPLY._serialized_start = 8595
    _EVENTSREPLY._serialized_end = 8655
    _ONORDERUPDATEREQUEST._serialized_start = 8657
    _ONORDERUPDATEREQUEST._serialized_end = 8691
    _ORDERUPDATESUMMARY._serialized_start = 8694
    _ORDERUPDATESUMMARY._serialized_end = 8884
    _ORDERUPDATEEVENTARGS._serialized_start = 8886
    _ORDERUPDATEEVENTARGS._serialized_end = 8978
    _ONORDERUPDATEREPLY._serialized_start = 8980
    _ONORDERUPDATEREPLY._serialized_end = 9076
    _ONQUOTEREQUEST._serialized_start = 9078
    _ONQUOTEREQUEST._serialized_end = 9106
    _ONQUOTEREPLY._serialized_start = 9108
    _ONQUOTEREPLY._serialized_end = 9194
    _ONTICKVALUEREQUEST._serialized_start = 9196
    _ONTICKVALUEREQUEST._serialized_end = 9228
    _SYMBOLTICKVALUE._serialized_start = 9230
    _SYMBOLTICKVALUE._serialized_end = 9282
    _ONTICKVALUEREPLY._serialized_start = 9284
    _ONTICKVALUEREPLY._serialized_end = 9375
    _ONORDERPROFITREQUEST._serialized_start = 9377
    _ONORDERPROFITREQUEST._serialized_end = 9411
    _PROFITUPDATE._serialized_start = 9414
    _PROFITUPDATE._serialized_end = 9545
    _ONORDERPROFITREPLY._serialized_start = 9547
    _ONORDERPROFITREPLY._serialized_end = 9637
    _ONQUOTEHISTORYREQUEST._serialized_start = 9639
    _ONQUOTEHISTORYREQUEST._serialized_end = 9674
    _QUOTEHISTORYEVENTARGS._serialized_start = 9676
    _QUOTEHISTORYEVENTARGS._serialized_end = 9782
    _ONQUOTEHISTORYREPLY._serialized_start = 9784
    _ONQUOTEHISTORYREPLY._serialized_end = 9884
    _ONDISCONNECTREQUEST._serialized_start = 9886
    _ONDISCONNECTREQUEST._serialized_end = 9919
    _ONDISCONNECTREPLY._serialized_start = 9921
    _ONDISCONNECTREPLY._serialized_end = 9987
    _CONNECTION._serialized_start = 12354
    _CONNECTION._serialized_end = 12567
    _MT4._serialized_start = 12570
    _MT4._serialized_end = 13756
    _SERVICE._serialized_start = 13759
    _SERVICE._serialized_end = 14229
    _SUBSCRIPTIONS._serialized_start = 14232
    _SUBSCRIPTIONS._serialized_end = 14932
    _TRADING._serialized_start = 14935
    _TRADING._serialized_end = 15293
    _STREAMS._serialized_start = 15296
    _STREAMS._serialized_end = 15597