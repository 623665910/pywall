from rules import register, SimpleRule
import netaddr


class IPRangeRule(SimpleRule):
    """Filter IP packets based on source/dest address."""
    def __init__(self, **kwargs):
        SimpleRule.__init__(self, **kwargs)
        self._ip_range = netaddr.IPNetwork(kwargs['cidr_range'])

class SourceIPRule(IPRangeRule):
    """Filter IP packets based on source address"""
    def __init__(self, **kwargs):
        IPRangeRule.__init__(self, **kwargs)
    
    def filter_condition(self, pywall_packet):
        """
        Filter packets if their source address falls within the ip_range.
        """
        return pywall_packet.get_src_ip() in self._ip_range

class DestinationIPRule(IPRangeRule):
    """Filter IP packets based on destination address"""
    def __init__(self, **kwargs):
        IPRangeRule.__init__(self, **kwargs)

    def filter_condition(self, pywall_packet):
        """
        Filter packets if their destination address falls within the ip_range."""
        return pywall_packet.get_dst_ip() in self._ip_range

register(SourceIPRule)
register(DestinationIPRule)
