function generateTimeRange(morningFrom, morningTo) {
    const timeRange = [];

    // Parse the time strings to Date objects
    const fromTime = new Date(`2000-01-01T${morningFrom}`);
    const toTime = new Date(`2000-01-01T${morningTo}`);

    // Set the initial time to the 'from' time
    let currentTime = fromTime;

    // Loop until the current time exceeds the 'to' time
    while (currentTime <= toTime) {
        // Calculate the end time by adding 10 minutes
        const endTime = new Date(currentTime);
        endTime.setMinutes(endTime.getMinutes() + 10);

        // Format the current time and end time as "HH:mm - HH:mm"
        const formattedTime = `${currentTime.toLocaleTimeString('en-US', { hour12: false, hour: 'numeric', minute: 'numeric' })} - ${endTime.toLocaleTimeString('en-US', { hour12: false, hour: 'numeric', minute: 'numeric' })}`;

        // Add the formatted time to the array
        timeRange.push(formattedTime);

        // Increment the current time by 10 minutes
        currentTime.setMinutes(currentTime.getMinutes() + 10);
    }

    return timeRange;
}

// Example usage:
const morningFrom = '09:12'; // Replace with the actual morningFrom time
const morningTo = '12:30';   // Replace with the actual morningTo time

const timeRange = generateTimeRange(morningFrom, morningTo);

console.log("\n\n----- Time Stamps -----\n\n");

for(let i = 0; i < timeRange.length; i++){
    console.log(timeRange[i]);
}
