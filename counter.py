from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame

class FourBitAnalyzer(HighLevelAnalyzer):
    result_types = {
        'four_bit_number': {
            'format': '4-bit number: {}',
            'type': 'text',
        }
    }

    def __init__(self):
        # Initialize the previous value as all zeros
        self.prev_value = 0

    def decode(self, frame):
        # Extract digital values from input channels
        bit0 = frame.data['D0']
        bit1 = frame.data['D1']
        bit2 = frame.data['D2']
        bit3 = frame.data['D3']

        # Interpret the 4 bits as a 4-bit binary number
        current_value = (bit3 << 3) | (bit2 << 2) | (bit1 << 1) | bit0

        if current_value != self.prev_value:
            # Calculate a new value when any bit changes
            new_value = current_value * 2  # Example calculation
            self.prev_value = current_value

            # Create an AnalyzerFrame with the result
            result_frame = AnalyzerFrame('four_bit_number', frame.start_time, frame.end_time)
            result_frame.data['four_bit_number'] = new_value
            self.queue_result(result_frame)

# Register your analyzer with Saleae Logic
FourBitAnalyzer.register()
