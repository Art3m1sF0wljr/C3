#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: QPSK_BPSK_toggle
# Author: Art3m1sF0wl
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import osmosdr
import time



from gnuradio import qtgui

class QPSK_BPSK_toggle(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "QPSK_BPSK_toggle", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("QPSK_BPSK_toggle")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "QPSK_BPSK_toggle")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.qpsk = qpsk = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j], [0, 1, 2, 3],
        4, 2, 2, 1, 1).base()
        self.nfilts = nfilts = 32
        self.bpsk = bpsk = digital.constellation_bpsk().base()
        self.access_key = access_key = '11100001010110101110100010010011'
        self.variable_qtgui_toggle_button_msg_0 = variable_qtgui_toggle_button_msg_0 = 0
        self.variable_adaptive_algorithm_0_0 = variable_adaptive_algorithm_0_0 = digital.adaptive_algorithm_cma( bpsk, .0001, sps).base()
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_cma( qpsk, .0001, sps).base()
        self.usrp_rate_1 = usrp_rate_1 = 768000
        self.transmit_button = transmit_button = 0
        self.thresh_0 = thresh_0 = 1
        self.thresh = thresh = 1
        self.sps_1 = sps_1 = 2
        self.sps_0_0 = sps_0_0 = 2
        self.sps_0 = sps_0 = 2
        self.sdr_samp_rate = sdr_samp_rate = 576000
        self.samp_rate = samp_rate = 576000
        self.rs_ratio_0 = rs_ratio_0 = 1.040
        self.rs_ratio = rs_ratio = 1.040
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.phase_bw_0 = phase_bw_0 = 0.0628
        self.phase_bw = phase_bw = 0.0628
        self.order_0 = order_0 = 2
        self.order = order = 4
        self.offset_freq = offset_freq = 200000
        self.modulation_toggle = modulation_toggle = 0
        self.hdr_format_0 = hdr_format_0 = digital.header_format_default(access_key, 0)
        self.hdr_format = hdr_format = digital.header_format_default(access_key, 0)
        self.freq_slider = freq_slider = 0
        self.excess_bw_0 = excess_bw_0 = 0.35
        self.excess_bw = excess_bw = 0.35
        self.access_key_0 = access_key_0 = '11100001010110101110100010010011'
        self.TXfrequency = TXfrequency = 415400000
        self.TX_rf_gain = TX_rf_gain = 40
        self.RXfrequency = RXfrequency = 415400000
        self.RX_rf_gain = RX_rf_gain = 40

        ##################################################
        # Blocks
        ##################################################

        self._transmit_button_choices = {'Pressed': 1, 'Released': 0}

        _transmit_button_toggle_button = qtgui.ToggleButton(self.set_transmit_button, 'TX', self._transmit_button_choices, False, 'value')
        _transmit_button_toggle_button.setColors("default", "default", "red", "default")
        self.transmit_button = _transmit_button_toggle_button

        self.top_layout.addWidget(_transmit_button_toggle_button)
        self._modulation_toggle_choices = {'Pressed': 1, 'Released': 0}

        _modulation_toggle_toggle_button = qtgui.ToggleButton(self.set_modulation_toggle, 'pressedBPSKred releasedQPSKgreen RX', self._modulation_toggle_choices, False, 'value')
        _modulation_toggle_toggle_button.setColors("green", "default", "red", "default")
        self.modulation_toggle = _modulation_toggle_toggle_button

        self.top_layout.addWidget(_modulation_toggle_toggle_button)
        self._freq_slider_range = Range(-1000000, 1000000, 1000, 0, 200)
        self._freq_slider_win = RangeWidget(self._freq_slider_range, self.set_freq_slider, "'freq_slider'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_slider_win)
        self._TXfrequency_tool_bar = Qt.QToolBar(self)
        self._TXfrequency_tool_bar.addWidget(Qt.QLabel("'TXfrequency'" + ": "))
        self._TXfrequency_line_edit = Qt.QLineEdit(str(self.TXfrequency))
        self._TXfrequency_tool_bar.addWidget(self._TXfrequency_line_edit)
        self._TXfrequency_line_edit.returnPressed.connect(
            lambda: self.set_TXfrequency(int(str(self._TXfrequency_line_edit.text()))))
        self.top_layout.addWidget(self._TXfrequency_tool_bar)
        self._TX_rf_gain_range = Range(0, 50, 1, 40, 200)
        self._TX_rf_gain_win = RangeWidget(self._TX_rf_gain_range, self.set_TX_rf_gain, "'TX_rf_gain'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._TX_rf_gain_win)
        self._RXfrequency_tool_bar = Qt.QToolBar(self)
        self._RXfrequency_tool_bar.addWidget(Qt.QLabel("'RXfrequency'" + ": "))
        self._RXfrequency_line_edit = Qt.QLineEdit(str(self.RXfrequency))
        self._RXfrequency_tool_bar.addWidget(self._RXfrequency_line_edit)
        self._RXfrequency_line_edit.returnPressed.connect(
            lambda: self.set_RXfrequency(int(str(self._RXfrequency_line_edit.text()))))
        self.top_layout.addWidget(self._RXfrequency_tool_bar)
        self._RX_rf_gain_range = Range(0, 50, 1, 40, 200)
        self._RX_rf_gain_win = RangeWidget(self._RX_rf_gain_range, self.set_RX_rf_gain, "'RX_rf_gain'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._RX_rf_gain_win)
        self._variable_qtgui_toggle_button_msg_0_choices = {'Pressed': 1, 'Released': 0}

        _variable_qtgui_toggle_button_msg_0_toggle_button = qtgui.ToggleButton(self.set_variable_qtgui_toggle_button_msg_0, 'variable_qtgui_toggle_button_msg_0', self._variable_qtgui_toggle_button_msg_0_choices, False, 'value')
        _variable_qtgui_toggle_button_msg_0_toggle_button.setColors("default", "default", "default", "default")
        self.variable_qtgui_toggle_button_msg_0 = _variable_qtgui_toggle_button_msg_0_toggle_button

        self.top_layout.addWidget(_variable_qtgui_toggle_button_msg_0_toggle_button)
        self.rational_resampler_xxx_0_2 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            415300000, #fc
            sdr_samp_rate, #bw
            "RX Waterfall", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            sdr_samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Mod Out QPSK", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_0_0_0_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "4_uscente da lin equalizer", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_y_axis((-1), 1)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "4_uscente da lin equalizer", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0.set_y_axis((-1), 1)
        self.qtgui_const_sink_x_0_0_0_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "1_source", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-1), 1)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.osmosdr_source_1 = osmosdr.source(
            args="numchan=" + str(1) + " " + "bladerf=0,nchan=1,buffers=48,transfers=24,agc_mode=manual"
        )
        self.osmosdr_source_1.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_1.set_sample_rate(sdr_samp_rate)
        self.osmosdr_source_1.set_center_freq((RXfrequency+freq_slider), 0)
        self.osmosdr_source_1.set_freq_corr(0, 0)
        self.osmosdr_source_1.set_dc_offset_mode(0, 0)
        self.osmosdr_source_1.set_iq_balance_mode(0, 0)
        self.osmosdr_source_1.set_gain_mode(False, 0)
        self.osmosdr_source_1.set_gain(RX_rf_gain, 0)
        self.osmosdr_source_1.set_if_gain(20, 0)
        self.osmosdr_source_1.set_bb_gain(20, 0)
        self.osmosdr_source_1.set_antenna('RX1', 0)
        self.osmosdr_source_1.set_bandwidth(0, 0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "bladerf=0,nchan=1,buffers=48,transfers=24,agc_mode=manual,biastee=1"
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(sdr_samp_rate)
        self.osmosdr_sink_0.set_center_freq((TXfrequency+freq_slider-offset_freq), 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(TX_rf_gain, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('TX1', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.digital_symbol_sync_xx_0_0 = digital.symbol_sync_cc(
            digital.TED_SIGNAL_TIMES_SLOPE_ML,
            sps,
            phase_bw,
            1.0,
            1.0,
            1.5,
            2,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_MF,
            32,
            rrc_taps)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_cc(
            digital.TED_MOD_MUELLER_AND_MULLER,
            sps,
            phase_bw,
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_MMSE_8TAP,
            128,
            [])
        self.digital_protocol_formatter_bb_0_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_map_bb_0_0 = digital.map_bb([0,1])
        self.digital_map_bb_0 = digital.map_bb([0,1,2,3])
        self.digital_linear_equalizer_0_0 = digital.linear_equalizer(15, 1, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_linear_equalizer_0 = digital.linear_equalizer(15, 2, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(4, digital.DIFF_DIFFERENTIAL)
        self.digital_crc32_bb_0_1 = digital.crc32_bb(False, "packet_len", True)
        self.digital_crc32_bb_0_0 = digital.crc32_bb(True, "packet_len", True)
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(phase_bw, order, False)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, order, False)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts("11100001010110101110100010010011",
          thresh, 'packet_len')
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=bpsk,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=qpsk,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(bpsk)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(qpsk)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(2)
        self.blocks_tagged_stream_mux_0_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'packet_len', 0)
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 252, "packet_len")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 252, "packet_len")
        self.blocks_selector_2 = blocks.selector(gr.sizeof_gr_complex*1,int(transmit_button),0)
        self.blocks_selector_2.set_enabled(True)
        self.blocks_selector_1 = blocks.selector(gr.sizeof_gr_complex*1,0,int(modulation_toggle))
        self.blocks_selector_1.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,int(modulation_toggle),0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(0.5)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(0.5)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/art3m1sf0wl/program/TRX_test/c3/test.txt', True, 0, 0)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/art3m1sf0wl/program/TRX_test/c3/LRPT_working/tx_data.bin', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/art3m1sf0wl/program/TRX_test/c3/test_out.txt', True)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/art3m1sf0wl/program/TRX_test/c3/LRPT_working/rx_data.bin', True)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, offset_freq, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_2, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.digital_crc32_bb_0_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.blocks_selector_2, 1))
        self.connect((self.blocks_selector_1, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_selector_1, 1), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.blocks_selector_2, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.digital_crc32_bb_0_1, 0))
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.blocks_repack_bits_bb_1, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_crc32_bb_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.digital_crc32_bb_0_1, 0), (self.blocks_tagged_stream_mux_0_0, 1))
        self.connect((self.digital_crc32_bb_0_1, 0), (self.digital_protocol_formatter_bb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_linear_equalizer_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_linear_equalizer_0, 0), (self.qtgui_const_sink_x_0_0_0_0_0, 0))
        self.connect((self.digital_linear_equalizer_0_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.digital_linear_equalizer_0_0, 0), (self.qtgui_const_sink_x_0_0_0_0_0_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0_0, 0), (self.blocks_tagged_stream_mux_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_linear_equalizer_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.digital_linear_equalizer_0, 0))
        self.connect((self.osmosdr_source_1, 0), (self.blocks_selector_1, 0))
        self.connect((self.osmosdr_source_1, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.osmosdr_source_1, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_symbol_sync_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_2, 0), (self.blocks_selector_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QPSK_BPSK_toggle")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_bpsk(self):
        return self.bpsk

    def set_bpsk(self, bpsk):
        self.bpsk = bpsk

    def get_access_key(self):
        return self.access_key

    def set_access_key(self, access_key):
        self.access_key = access_key
        self.set_hdr_format(digital.header_format_default(self.access_key, 0))
        self.set_hdr_format_0(digital.header_format_default(self.access_key, 0))

    def get_variable_qtgui_toggle_button_msg_0(self):
        return self.variable_qtgui_toggle_button_msg_0

    def set_variable_qtgui_toggle_button_msg_0(self, variable_qtgui_toggle_button_msg_0):
        self.variable_qtgui_toggle_button_msg_0 = variable_qtgui_toggle_button_msg_0

    def get_variable_adaptive_algorithm_0_0(self):
        return self.variable_adaptive_algorithm_0_0

    def set_variable_adaptive_algorithm_0_0(self, variable_adaptive_algorithm_0_0):
        self.variable_adaptive_algorithm_0_0 = variable_adaptive_algorithm_0_0

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_usrp_rate_1(self):
        return self.usrp_rate_1

    def set_usrp_rate_1(self, usrp_rate_1):
        self.usrp_rate_1 = usrp_rate_1

    def get_transmit_button(self):
        return self.transmit_button

    def set_transmit_button(self, transmit_button):
        self.transmit_button = transmit_button
        self.blocks_selector_2.set_input_index(int(self.transmit_button))

    def get_thresh_0(self):
        return self.thresh_0

    def set_thresh_0(self, thresh_0):
        self.thresh_0 = thresh_0

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh

    def get_sps_1(self):
        return self.sps_1

    def set_sps_1(self, sps_1):
        self.sps_1 = sps_1

    def get_sps_0_0(self):
        return self.sps_0_0

    def set_sps_0_0(self, sps_0_0):
        self.sps_0_0 = sps_0_0

    def get_sps_0(self):
        return self.sps_0

    def set_sps_0(self, sps_0):
        self.sps_0 = sps_0

    def get_sdr_samp_rate(self):
        return self.sdr_samp_rate

    def set_sdr_samp_rate(self, sdr_samp_rate):
        self.sdr_samp_rate = sdr_samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.sdr_samp_rate)
        self.osmosdr_source_1.set_sample_rate(self.sdr_samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.sdr_samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(415300000, self.sdr_samp_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_rs_ratio_0(self):
        return self.rs_ratio_0

    def set_rs_ratio_0(self, rs_ratio_0):
        self.rs_ratio_0 = rs_ratio_0

    def get_rs_ratio(self):
        return self.rs_ratio

    def set_rs_ratio(self, rs_ratio):
        self.rs_ratio = rs_ratio

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_phase_bw_0(self):
        return self.phase_bw_0

    def set_phase_bw_0(self, phase_bw_0):
        self.phase_bw_0 = phase_bw_0

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)
        self.digital_costas_loop_cc_0_0.set_loop_bandwidth(self.phase_bw)
        self.digital_symbol_sync_xx_0.set_loop_bandwidth(self.phase_bw)
        self.digital_symbol_sync_xx_0_0.set_loop_bandwidth(self.phase_bw)

    def get_order_0(self):
        return self.order_0

    def set_order_0(self, order_0):
        self.order_0 = order_0

    def get_order(self):
        return self.order

    def set_order(self, order):
        self.order = order

    def get_offset_freq(self):
        return self.offset_freq

    def set_offset_freq(self, offset_freq):
        self.offset_freq = offset_freq
        self.analog_sig_source_x_0.set_frequency(self.offset_freq)
        self.osmosdr_sink_0.set_center_freq((self.TXfrequency+self.freq_slider-self.offset_freq), 0)

    def get_modulation_toggle(self):
        return self.modulation_toggle

    def set_modulation_toggle(self, modulation_toggle):
        self.modulation_toggle = modulation_toggle
        self.blocks_selector_0.set_input_index(int(self.modulation_toggle))
        self.blocks_selector_1.set_output_index(int(self.modulation_toggle))

    def get_hdr_format_0(self):
        return self.hdr_format_0

    def set_hdr_format_0(self, hdr_format_0):
        self.hdr_format_0 = hdr_format_0

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_freq_slider(self):
        return self.freq_slider

    def set_freq_slider(self, freq_slider):
        self.freq_slider = freq_slider
        self.osmosdr_sink_0.set_center_freq((self.TXfrequency+self.freq_slider-self.offset_freq), 0)
        self.osmosdr_source_1.set_center_freq((self.RXfrequency+self.freq_slider), 0)

    def get_excess_bw_0(self):
        return self.excess_bw_0

    def set_excess_bw_0(self, excess_bw_0):
        self.excess_bw_0 = excess_bw_0

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_access_key_0(self):
        return self.access_key_0

    def set_access_key_0(self, access_key_0):
        self.access_key_0 = access_key_0

    def get_TXfrequency(self):
        return self.TXfrequency

    def set_TXfrequency(self, TXfrequency):
        self.TXfrequency = TXfrequency
        Qt.QMetaObject.invokeMethod(self._TXfrequency_line_edit, "setText", Qt.Q_ARG("QString", str(self.TXfrequency)))
        self.osmosdr_sink_0.set_center_freq((self.TXfrequency+self.freq_slider-self.offset_freq), 0)

    def get_TX_rf_gain(self):
        return self.TX_rf_gain

    def set_TX_rf_gain(self, TX_rf_gain):
        self.TX_rf_gain = TX_rf_gain
        self.osmosdr_sink_0.set_gain(self.TX_rf_gain, 0)

    def get_RXfrequency(self):
        return self.RXfrequency

    def set_RXfrequency(self, RXfrequency):
        self.RXfrequency = RXfrequency
        Qt.QMetaObject.invokeMethod(self._RXfrequency_line_edit, "setText", Qt.Q_ARG("QString", str(self.RXfrequency)))
        self.osmosdr_source_1.set_center_freq((self.RXfrequency+self.freq_slider), 0)

    def get_RX_rf_gain(self):
        return self.RX_rf_gain

    def set_RX_rf_gain(self, RX_rf_gain):
        self.RX_rf_gain = RX_rf_gain
        self.osmosdr_source_1.set_gain(self.RX_rf_gain, 0)




def main(top_block_cls=QPSK_BPSK_toggle, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
