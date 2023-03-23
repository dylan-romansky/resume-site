import { TestBed } from '@angular/core/testing';

import { ResItService } from './res-it.service';

describe('ResItService', () => {
  let service: ResItService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ResItService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
