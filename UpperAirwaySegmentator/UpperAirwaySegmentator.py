import slicer
from slicer.ScriptedLoadableModule import *

from UpperAirwaySegmentatorLib import SegmentationWidget


class UpperAirwaySegmentator(ScriptedLoadableModule):
    def __init__(self, parent):
        from slicer.i18n import tr, translate
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = tr("UpperAirwaySegmentator")
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "Segmentation")]
        self.parent.dependencies = []
        self.parent.contributors = [
            "Alejandro Matos Camarillo (uAlberta)",
            "Silvia Capenakas (uAlberta)",
            "Manuel Lagravere (uAlberta)"
        ]

        self.parent.helpText = tr(
            "Fully automatic AI segmentation tool for CBCT scans based on UpperAirwaySegmentator nnU-Net "
            "model."
        )
        self.parent.acknowledgementText = tr(
            "This module was originally developed at the"
            '<a href="https://www.ualberta.ca/school-of-dentistry/">University of Alberta</a> '
            "(uAlberta) for the analysis of orthodontic data."
        )


class UpperAirwaySegmentatorWidget(ScriptedLoadableModuleWidget):
    def __init__(self, parent=None) -> None:
        ScriptedLoadableModuleWidget.__init__(self, parent)
        self.logic = None

    def setup(self) -> None:
        """Called when the user opens the module the first time and the widget is initialized."""
        ScriptedLoadableModuleWidget.setup(self)
        widget = SegmentationWidget()
        self.logic = widget.logic
        self.layout.addWidget(widget)
        self.layout.addStretch()


class UpperAirwaySegmentatorTest(ScriptedLoadableModuleTest):
    def runTest(self):
        try:
            from SlicerPythonTestRunnerLib import RunnerLogic, RunnerWidget, RunSettings, isRunningInTestMode
            from pathlib import Path
        except ImportError:
            slicer.util.warningDisplay("Please install SlicerPythonTestRunner extension to run the self tests.")
            return

        currentDirTest = Path(__file__).parent.joinpath("Testing")
        results = RunnerLogic().runAndWaitFinished(
            currentDirTest,
            RunSettings(extraPytestArgs=RunSettings.pytestFileFilterArgs("*TestCase.py") + ["-m not slow"]),
            doRunInSubProcess=not isRunningInTestMode()
        )

        if results.failuresNumber:
            raise AssertionError(f"Test failed: \n{results.getFailingCasesString()}")

        slicer.util.delayDisplay(f"Tests OK. {results.getSummaryString()}")
