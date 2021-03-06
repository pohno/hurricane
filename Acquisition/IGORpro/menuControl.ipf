#pragma rtGlobals=1		// Use modern global access method.

Menu "Photon Counter"

	Submenu "Communications"
	"Open", openSRS()
	"Check", checkSRS()
	"Close", closeSRS()
	End
	
	Submenu "Valve and pump control"
	"Initialize Pump and Valve Settings", initPumpValveSettings()
	"Flow Control Panel", flowControlPanel()
	"Flow Rate Panel",flowRatePanel()
	End
	
	Submenu "Stored Photon Counter Settings"
	"GEO4: OPA- Juli, Alicia, Mavis?", recallGPCParameters(1)
	"MHZ- Paul and Sarah", recallGPCParameters(2)
	"LIQAIR2", recallGPCParameters(3)
	"GEOMHZ", recallGPCParameters(4)
	End	
	
	Submenu "Scan"
		"Scan Control Panel", scanControl()
		"Start Fixed Length", startScan(0)
		"Start Continuous", startScan(1)
		"Pause/F4", stopScan()
		"Resume/F5", resumeScan()
		"Stop and Reset", resetScan()
		"Set Next Pause/F6",setNextPause()
	End
	Submenu "Wave Analysis"
		"Find Average", findAverage()
	End
		
end
