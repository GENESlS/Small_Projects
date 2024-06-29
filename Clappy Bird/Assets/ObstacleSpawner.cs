using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObstacleSpawner : MonoBehaviour
{
    public GameObject pipePrefab;
    public Transform bird;
    public float spawnInterval = 2f;
    public float minYGap = -2f;
    public float maxYGap = 2f;
    public float spawnDistance = 10f;
    public float timer = 5f;

    private float timeSinceLastSpawn;

    void Start()
    {
        timeSinceLastSpawn = 0f;
    }

    void Update()
    {
        timeSinceLastSpawn += Time.deltaTime;

        if (timeSinceLastSpawn >= spawnInterval)
        {
            SpawnPipe();
            timeSinceLastSpawn = 0f;
        }
    }

    void SpawnPipe()
    {
        Debug.Log("SpawnPipe called");
        float gapYPosition = Random.Range(minYGap, maxYGap);
        Vector3 spawnPosition = new Vector3(bird.position.x + spawnDistance, gapYPosition, 0);

        GameObject instance = Instantiate(pipePrefab, spawnPosition, Quaternion.identity);
        
        if (instance != null)
    {
        Debug.Log("Instance created"); // This will log a message every time an instance is successfully created

        // Add the DestroyOnTimer component to the instantiated object
        DestroyOnTimer destroyOnTimer = instance.AddComponent<DestroyOnTimer>();

        // Set the timer value
        destroyOnTimer.timer = timer;
    }
    else
    {
        Debug.Log("Instance creation failed"); // This will log a message if the instance creation fails
    }
    }
    
}
